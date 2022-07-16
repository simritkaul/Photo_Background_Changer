def validInput(pos_w, pos_h, scale, bg_w, bg_h, sub_w, sub_h):
  sub_wnew = round(sub_w * scale)
  sub_hnew = round(sub_h * scale)

  if sub_wnew >= bg_w or sub_hnew >= bg_h:
    return False

  if pos_w >= bg_w or pos_h >= bg_h:
    return False

  if pos_w + sub_wnew >= bg_w or pos_h + sub_hnew >= bg_h:
    return False

  return True