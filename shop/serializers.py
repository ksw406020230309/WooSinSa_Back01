from rest_framework import serializers
from shop.models import Product, ProductQuestion, AdminComment



# ============== 상품 게시글 시작 ================
# 23년 6월 12일
# 상품 리스트
class ProductListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return {"nickname": obj.user.username, "id": obj.user.id, "product_img": str(obj.user.product_img)}

    class Meta:
        model = Product
        fields = ["id", "product_name", "product_price", "product_stuck", "product_explane", "product_img", "user", "hearts"]

# 23년 6월 12일
# 상품 게시글 작성
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_name", "product_price", "product_stuck", "product_explane", "product_img"
            ]
        extra_kwargs={
            "product_name": {
                "error_messages": {
                    "blank": "상품 이름을 입력해주세요",
                }
            },
            "product_price": {
                "error_messages": {
                    "blank": "상품 가격을 입력해주세요",
                },
            },
            "product_stuck": {
                "error_messages": {
                    "blank": "재고 수량을 입력해주세요",
                },
            },
            "product_explane": {
                "error_messages": {
                    "blank": "상품 설명을 입력해주세요",
                },
            },
            "product_img": {
                "error_messages": {
                    "blank": "상품 사진을 입력해주세요",
                },
            },
        }


# 23년 6월 12일
# 상품 삭제 시리얼라이저
class ProductDeleteSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    class Meta:
        model = Product
        fields = ['content',]
# ============== 상품 게시글 끝 ================



# ============== 상품 문의 시작 ================
# 23년 6월 12일
# 상품 문의 생성 시리얼라이저
class QuestionCreateSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_product(self, obj):
        return {"product_name": obj.product.product_name, "id": obj.product.id}

    def get_user(self, obj):
        return {"username": obj.user.username, "id": obj.user.id}

    class Meta:
        model = ProductQuestion
        fields = [
            "product", "product_name", "question_title", "question_content"
            ]
        extra_kwargs={
            "question_title": {
                "error_messages": {
                    "blank": "상품 이름을 입력해주세요",
                }
            },
            "question_content": {
                "error_messages": {
                    "blank": "상품 가격을 입력해주세요",
                },
            },
        }

# 23년 6월 12일
# 상품 문의 모아보기 시리얼라이저
class QuestionListserializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return {"username": obj.user.username, "id": obj.user.id}

    class Meta:
        model = ProductQuestion
        fields = ["question_title", "question_content", "is_complete"]

# ============== 상품 문의 끝 ================

# 23년 6월 12일
# 상품 상세보기 시리얼라이저
class ProductDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product_question = QuestionListserializer(many=True)
    like_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {"username": obj.user.username, "id": obj.user.id}

    def get_like_count(self, obj):
        return obj.like_count.count()

    class Meta:
        model = Product
        fields = "__all__"

# ============== 관리자 답변 시리얼라이저 시작 ================
# 23년 6월 12일
# 관리자 댓글 생성 시리얼라이저
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminComment
        fields = [
            "question_title", "question_content"
            ]
        extra_kwargs={
            "question_title": {
                "error_messages": {
                    "blank": "상품 이름을 입력해주세요",
                }
            },
            "question_content": {
                "error_messages": {
                    "blank": "상품 가격을 입력해주세요",
                },
            },
        }

# 23년 6월 12일
# 관리자 댓글 보기 시리얼라이저
class CommentListserializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return {"username": obj.user.username, "id": obj.user.id}

    class Meta:
        model = AdminComment
        fields = ["id", "question_title", "question_content"]

# ============== 관리자 답변 시리얼라이저 끝 ================
