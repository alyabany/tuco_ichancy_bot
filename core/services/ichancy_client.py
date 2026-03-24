import aiohttp
import time

class IchancyClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session_cookie = None
        self.last_login = 0

    async def login(self):
        url = "https://agents.ichancy.com/global/api/User/signIn"
        payload = {"username": self.username, "password": self.password}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                cookies = resp.cookies
                for name, cookie in cookies.items():
                    if "PHPSESSID" in name:
                        self.session_cookie = f"{name}={cookie.value}"
                        self.last_login = time.time()
                        return True
        return False

    async def ensure_login(self):
        # إذا مر وقت طويل أو ما في كوكي → اعمل تسجيل دخول
        if not self.session_cookie or (time.time() - self.last_login > 1800):
            await self.login()

    async def create_player(self, email, password, parent_id, login):
        await self.ensure_login()

        url = "https://agents.ichancy.com/global/api/Player/registerPlayer"
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.session_cookie
        }

        payload = {
            "player": {
                "email": email,
                "password": password,
                "parentId": str(parent_id),
                "login": login
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                data = await resp.json()
                print(data)
                if resp.status != 200:
                    return {"error": f"HTTP {resp.status}"}
                
                if data.get("status") != True:
                    return {
                        "success" : 0,
                        "error": f"HTTP {resp.status}"
                        }
                else:
                    return {
                        "success" : 1,
                        "error" : 0,
                    }

    async def get_players(self):
        await self.ensure_login()

        url = "https://agents.ichancy.com/global/api/Player/getPlayersForCurrentAgent"
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.session_cookie
        }

        payload = {
            "page": 1,
            "pageSize": 9999,
            "search": "",
            "sortField": "",
            "sortOrder": ""
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                data = await resp.json()
                print(data)

                if resp.status != 200:
                    return {"success": 0, "error": f"HTTP {resp.status}"}

                if data.get("status") != True:
                    return {"success": 0, "error": "API returned error"}

                return {
                    "success": 1,
                    "error": 0,
                    "players": data["result"]["records"]
                }
    
    async def get_player_id_by_username(self, username: str):
        result = await self.get_players()

        if result["success"] != 1:
            return None

        players = result["players"]

        for p in players:
            if p["username"] == username:
                return p["playerId"]

        return None




    async def deposit_player(self, player_id: str, amount: int, comment=None):
        await self.ensure_login()

        url = "https://agents.ichancy.com/global/api/Player/depositToPlayer"
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.session_cookie
        }

        payload = {
            "amount": amount,
            "comment": comment,
            "playerId": str(player_id),
            "currencyCode": "NSP",
            "currency": "NSP",
            "moneyStatus": 5
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                data = await resp.json()
                print(data)

                if resp.status != 200:
                    return {"success": 0, "error": f"HTTP {resp.status}"}

                if data.get("status") != True:
                    return {"success": 0, "error": "API returned error"}

                return {"success": 1, "error": 0}
                    
    async def withdraw_player(self, player_id: str, amount: int, comment=None):
        await self.ensure_login()

        url = "https://agents.ichancy.com/global/api/Player/withdrawFromPlayer"
        headers = {
            "Content-Type": "application/json",
            "Cookie": self.session_cookie
        }

        payload = {
            "amount": -abs(amount),  # دائماً سالب
            "comment": comment,
            "playerId": str(player_id),
            "currencyCode": "NSP",
            "currency": "NSP",
            "moneyStatus": 5
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                data = await resp.json()
                print(data)

                if resp.status != 200:
                    return {"success": 0, "error": f"HTTP {resp.status}"}

                if data.get("status") != True:
                    return {"success": 0, "error": "API returned error"}

                return {"success": 1, "error": 0}

ichancy = IchancyClient("Yabany@agent.nsp", "Yabany@21")