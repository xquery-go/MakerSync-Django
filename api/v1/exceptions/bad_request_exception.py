class BadRequestException(Exception):
    
    def __init__(self, status=404, detail="Bad Request"):
        self.status=status
        self.detail=detail
        
        super().__init__()