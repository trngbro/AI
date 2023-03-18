'''

HÀM BFS:
  Khởi tạo queue và đánh dấu trạng thái ban đầu
  WHILE queue chưa rỗng:
    Lấy trạng thái đầu tiên trong queue
    Nếu đó là trạng thái kết thúc thì trả về lời giải
    Duyệt tất cả các trạng thái kế tiếp của trạng thái hiện tại:
      Nếu trạng thái chưa được đánh dấu:
        Đánh dấu trạng thái và thêm vào queue
  Nếu không tìm thấy lời giải thì trả về None
  
'''

