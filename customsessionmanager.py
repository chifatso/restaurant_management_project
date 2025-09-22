import time

class SessionManager:
    def __init__(self, expiry_seconds):
        """
        Initialize the session manager.
        :param expiry_seconds: Number of seconds a session should remain active.
        """
        self.expiry_seconds = expiry_seconds
        #Dictionary to store sessions: {session_id: creation_timestamp}
        self.sessions = {}

    def create_session(self, session_id):
        """
        Create a new session.
        Stores the session_id with the current timestamp
        """
        self.sessions[session_id] = time.time()
        return f"Session {session_id} created."
    
    def is_session_active(self, session_id):
        """
        Check if session is still active.
        -Returns True if session exists and has not expired.
        -If expired, deletes it and returns false.
        -If not found, returns false.
        """
        if session_id not in self.sessions:
            return False
        
        created_at = self.sessions[session_id]
        now = time.time()

        if now-created_at > self.expiry_seconds:
            #Automatically remove expired session
            del self.sessions[session_id]
            return False
        return True
    
    def delete_session(self, session_id):
        """
        Delete a session manually.
        Simulates logout or forced logout.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return "Deleted"
        return "Not Found"