# Workflow

* New Student
    1. User Register
        1. App started, welcome screen.
        2. Choose "register", show register screen.
        3. Fill in "username", "email", "password", send `register` message.
        4. Server make sure `username` and `email` is valid, send `register-result` message back.
        5. If the result is negative, show the info.
        6. Other wise, forward to "login" screen.
    
    2. User login
        1. User choose login, fill in "username" and "password", send `login` message.
        2. Server verify the password, send `login-result` message back.
        3. If failed, show the error message.
        4. Otherwise, save the login token and forward to "user home" screen.
        
    3. User home
        1. Retrieve the book list of the user by sending `getBookList` message.
        2. Show the books in "home screen" (see google document for UI)
        3. User open a book by clicking on its title.
        
    4. Book view
        1. Retrieve the book contents by sending `getBook` message.
        2. Book contents consist a list of `Cell`s.
        
            A `Cell` is a segment of the book. It can be created in different formats: "img", "md", "latex", "asccimath" or other formats.
            
            User can add, edit, move or delete a cell.
        3. To add contents to the book, the student choose "add Cell".
    5. Cell editor
        1. User can set the format of the cell.
        2. User can edit the contents of the cell.
        3. There should be preview of the editing cell.
        4. When the user is satisfied about the content, she can `save` the cell.
        5. A `save-cell` message is sent to the server, with "format", "content", "rendered", the message also includes the "bookid", "previous-cell".
        6. Server will validate the data, save them into `Cell` table. Reply with `save-cell-result` message.
        7. The server will also sent the change of the book to all users who are currently reading the book, include the book owner, and any teachers who is reading the book.
        
            A change set of the book contains a list of cell, each cell might be modified in someway: it may get new content, or its `previous-cell` is changed (order of cells changed).
        8. After a user received the change set, it will be applied the book.
    6. Question and Answer
        A cell may also be marked as a "question" cell, such cells will be saved as usual, in addition to that, it will also trigger a new notice to the teachers, notifying them that a new question is posted. 
        
        The questions are ordered in a line according to their submit time, the student will be updated about the position of her question in the line.
        
        This will be detailed in the following "Teacher" section.
        
* Teacher
    1. Teacher Register
        
        It's the same procedure as student.
        
    2. Teacher login
        
        The teacher login through the same procedure as student, but after logged in, the teacher will receive a list of unanswered questions. The questions are listed in the order of their creation time.
        
    3. Answering the question
    
        The teacher can open a question, answer it by creating a new cell, then send the answer back. The times of when the teacher started and finished the answer are also record, which will be used for billing purpose.
        
        1. The teacher opens a question.
        2. A cell editor allows the teacher to compose the answer.
        3. After the teacher completed the question, an `answer` message is sent.
        4. Server will save the answer to the book, notify the student about the answer, also send updates of their position change to the students who is waiting in line.
        
    4. Viewing student's Books
        
        The books of the students are public to the teachers. The teacher can see the list of students, open their book shelf, and see the contents of the books.
