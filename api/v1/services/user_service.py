from api.v1.schemas import UserRequestSchema, UserResponseSchema
from api.v1.repositories import UserRepository
from api.v1.exceptions import BadRequestException, NotFoundException, ServerErrorException
class UserService:
    
    @staticmethod    
    def list(sensor_id : str):
        pass
    
    
    @staticmethod    
    def create(sensor_id : str, user_request: UserRequestSchema):
        
        email=user_request.email
        if UserRepository.is_user_exists(sensor_id, email):
            raise BadRequestException(
                detail="User already exists."
            )
        
        if not UserRepository.create_user(sensor_id, user_request):
            raise ServerErrorException()
        
        return UserResponseSchema(**user_request.dict())
    
    
    @staticmethod    
    def retrieve(sensor_id : str, email : str):
        
        if not UserRepository.is_user_exists(sensor_id, email):
            return NotFoundException(
                detail="User does not exist."
            )
        
        user=UserRepository.get_user(sensor_id, email)
        if not user:
            return BadRequestException(
                detail="Invalid user email."
            )
        
        return UserResponseSchema(**user)

    
    
    @staticmethod    
    def update(sensor_id : str, email : str):
        pass
    
    
    @staticmethod    
    def destroy(sensor_id : str, email : str):
        pass