

# def repeat_quest_double_quest(device, debug=False):
#     LIMIT = 19
#     count = 0
#     for x in range(LIMIT):
#         base = device.takeSnapshot()
#         tap(device, Elements.quest_loc_sm, timeout=1)
#         tap(device, Elements.qs_done, offset=5, timeout=1)
#         tap(device, Elements.qs_done_alt, offset=5, timeout=1)
#         tap(device, Elements.qs_dia_loc, timeout=1)

#         check_exit(device)

#         accept = check_image(base, Elements.qs_accept, debug=debug)
#         if accept:
#             tap_till_gone(device, Elements.qs_accept, timeout=1)
#             tap(device, Elements.qs_dia_loc, timeout=2)
#             count += 1
#             if count == 2:
#                 return

#     check_exit(device)


# BUG: When character stops moving upon landing
# while 1:
#     base = device.takeSnapshot()
#     if check_image(base, Elements.flip_btn, debug=debug) or check_image(
#         base, Elements.flip_2_btn, debug=debug
#     ):
#         MonkeyRunner.sleep(1)
#         go_back(device, False, location)
#         break
#     else:
#         device.touch(0, 0, "DOWN")
#         MonkeyRunner.sleep(1)


# Won't fucking need this anymore because, BP is already 40M :/
# def go_market(device, debug, minutes=30):
#     tap_wait(
#         device,
#         Elements.mkt_hamburger,
#         Elements.mkt_market_btn,
#         tolerance=0.10,
#         timeout=1,
#     )
#     tap_wait(
#         device, Elements.mkt_market_btn, Elements.exit_menu, timeout=2, max_retries=2
#     )
#     device.drag((200, 980), (200, 300), 1, 50)
#     tap(device, Elements.mkt_consumables_btn)
#     tap(device, Elements.mkt_others)

#     base = device.takeSnapshot()
#     if not check_image(base, Elements.black_pearls, debug=debug):
#         tap(device, Elements.exit_menu)
#         return

#     tap(device, Elements.mkt_black_pearls)
#     MonkeyRunner.sleep(1)
#     # Anti Bug
#     base = device.takeSnapshot()
#     if not check_image(base, Elements.flavor_text, debug=debug):
#         log("BUG BUG BUG BUG BUG BUG BUG")
#         tap(device, Elements.exit_menu)
#         return

#     COMMON_TIMEOUT = 0.3
#     # 3 seconds turn around to click the first location
#     max_retries = (minutes * 60) / 1.5
#     for i in range(max_retries):
#         # Anti Bug
#         # if i % 5 == 0:
#         #     base = device.takeSnapshot()
#         #     if not check_image(base, Elements.flavor_text, debug=debug):
#         #         log("[2] BUG BUG BUG BUG BUG BUG BUG")
#         #         tap(device, Elements.exit_menu)
#         #         return

#         log("Retry Loop: " + str(i) + "/" + str(max_retries))
#         tap(device, Elements.mkt_refresh_loc, timeout=COMMON_TIMEOUT)
#         tap(device, Elements.mkt_bid_loc_1, timeout=COMMON_TIMEOUT)
#         # tap(device, Elements.mkt_bid_loc_2)
#         # tap(device, Elements.mkt_bid_loc_3)
#         tap(device, Elements.mkt_max, timeout=COMMON_TIMEOUT)
#         tap(device, Elements.mkt_calc_confirm, timeout=COMMON_TIMEOUT)
#     tap(device, Elements.exit_menu)