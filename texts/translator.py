from texts.texts import texts

def t(event_or_user, key, **kwargs):
    # إذا كان event (Message أو CallbackQuery)
    if hasattr(event_or_user, "from_user"):
        user_id = event_or_user.from_user.id
    else:
        # إذا كان رقم user_id مباشرة
        user_id = event_or_user

    #lang =  get_language(user_id)
    text = texts[key]
    return text.format(**kwargs)

def t_user(key, **kwargs):

    if kwargs.user_id :
        lang = "ar"
    text = texts[key]
    return text.format(**kwargs)
