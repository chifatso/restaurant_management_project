import time
import uuid #For generating unique session ids

class SessionManager:
    def __init__(self, session_timeout = 60):
        """ 
        Initialize the session manager.
        session_timeout: lifetime of each session in seconds.
        sessions: dictionary to store active sessions.
        key: session_id (unique string)
        value: expiry timestamp (float from time.time())

        """
        self.session_timeout = session_timeout
        self.sessions = {}

    def create_session(self, user_id):
        """
        Create a new session for a user with an expiry time.
        Returns the session_id.

        """
        session_id = str(uuid.uuid4()) #Generate a unique session ID
        expiry_time = time.time() + self.session_timeout #Set expiry timestamp
        self.sessions[session_id] = {"user_id":user_id, "expiry":expiry_time}
        return session_id
    
    def is_session_active(self, session_id):
        """
        Check if session is still valid (not expired).
        Expired sessions are removed automatically.
        Returns True if active, False otherwise.

        """
        self.cleanup_sessions() #remove expired sessions first

        if session_id in self.sessions:
            #Session exists and is still valid
            return True
        else:
            #Session not found or expired
            return False
        
    def cleanup_sessions(self):
        """
        Remove all expired sessions from memory.

        """
        current_time = time.time()
        expired = [
            sid for sid, data in self.sessions.items()
            if data["expiry"] < current_time
        ]

        for sid in expired:
            del self.sessions[sid] #deleted expired session
        
    def get_user_from_session(self, session_id):
        """
        Return the user_id associated with a valid session.
        If session is expired or not found return None.

        """
        if self.is_session_active(session_id):
            return self.sessions[session_id]["user_id"]
        return None

