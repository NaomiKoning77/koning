from seleniumbase import SB

with SB(uc=True, test=True) as naomi:

    if True:
        url = "https://kick.com/brutalles"
        naomi.uc_open_with_reconnect(url, 5)
        naomi.uc_gui_click_captcha()
        naomi.sleep(1)
        naomi.uc_gui_handle_captcha()
        naomi.sleep(1)
        if naomi.is_element_present('button:contains("Accept")'):
            naomi.uc_click('button:contains("Accept")', reconnect_time=4)
        if naomi.is_element_visible('#injected-channel-player'):
            while naomi.is_element_visible('#injected-channel-player'):
                naomi.sleep(10)
