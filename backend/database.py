# Database Connection and Session Management

# Import necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Chuỗi kết nối đến cơ sở dữ liệu (SQLAlchemy)
# Đây là nơi bạn sẽ đặt thông tin kết nối đến cơ sở dữ liệu của bạn.
# Ví dụ: 'sqlite:///example.db' cho SQLite hoặc 'postgresql://user:password@localhost/dbname' cho PostgreSQL.
DATABASE_URL = "sqlite:///./test.db"

# Tạo engine cho SQLAlchemy dựa trên chuỗi kết nối
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo SessionLocal để quản lý session cho cơ sở dữ liệu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Khai báo Base để sử dụng cho các mô hình
Base = declarative_base()

# Định nghĩa hàm tạo session
# Hàm này sẽ trả về một session (kết nối đến cơ sở d�� liệu) cho bạn sử dụng
# Hãy nhớ đóng session khi không sử dụng nữa để tránh rò rỉ tài nguyên.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()