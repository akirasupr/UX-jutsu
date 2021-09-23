# tools for jutsu plugins by @Kakashi_HTK(tg)/@ashwinstr(gh)


from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import (
    InputPeerUserFromMessage,
    InputReportReasonPornography,
    InputReportReasonSpam,
)


# capitalise
def capitaled(query: str):
    query_split = query.split()
    cap_text = []
    for word_ in query_split:
        word_cap = word_.capitalize()
        cap_text.append(word_cap)
    cap_query = " ".join(cap_text)
    return cap_query


# to report for spam or pornographic content
def report_user(chat: int, user_id: int, msg: dict, msg_id: int, reason: str):
    if ("nsfw" or "porn") in reason:
        reason_ = InputReportReasonPornography()
        for_ = "pornographic message"
    else:
        reason_ = InputReportReasonSpam()
        for_ = "spam message"
    peer_ = (
        InputPeerUserFromMessage(
            peer=chat,
            msg_id=msg_id,
            user_id=user_id,
        ),
    )
    ReportPeer(
        peer=peer_,
        reason=reason_,
        message=msg,
    )
    return for_


# return time and date after applying time difference
def time_date(year: int, month: int, date: int, hour: int, minute: int, diff: str):
    """time and date changer as per time-zone difference"""
    differ = diff.split(":")
    if int(differ[0]) >= 12 or int(differ[0]) <= -12 or int(differ[1]) >= 60:
        return "`Format of the difference given is wrong, check and try again...`"
    try:
        hour_diff = differ[0]
        hour_diff = int(hour_diff)
        min_diff = differ[1]
        min_diff = int(min_diff)

        if hour_diff < 0:
            minute -= min_diff
            if minute < 0:
                minute += 60
                hour -= 1
            hour -= hour_diff
            if hour < 0:
                date -= 1
                hour += 12
            elif hour > 12 and hour < 24:
                hour -= 12
            elif hour == 12:
                pass
            else:
                pass
            if date < 1:
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
                if month == (12 or 10 or 8 or 7 or 5 or 3 or 1):
                    date = 31
                elif month == (11 or 9 or 6 or 4):
                    date = 30
                else:
                    if year % 4 == 0:
                        date = 29
                    else:
                        date = 28
        else:
            minute += min_diff
            if minute >= 60:
                hour += 1
                if hour > 12 and hour < 24:
                    hour -= 12
                elif hour == 12:
                    pass
                elif hour >= 24:
                    hour -= 24
                    date += 1
                    if date > 30 and (month == (4 or 6 or 9 or 11)):
                        month += 1
                    elif date > 28 and month == 2 and year % 4 != 0:
                        month += 1
                    elif date > 29 and month == 2 and year % 4 == 0:
                        month += 1
                    elif date > 31 and (month == (1 or 3 or 5 or 7 or 8 or 10 or 12)):
                        month += 1
                        if month > 12:
                            year += 1
        hour = f"{hour:02}"
        minute = f"{minute:02}"
        date = f"{date:02}"
        month = f"{month:02}"
        json_ = {
            "min": minute,
            "hour": hour,
            "date": date,
            "month": month,
            "year": year,
        }
        return json_
    except Exception as e:
        return e
