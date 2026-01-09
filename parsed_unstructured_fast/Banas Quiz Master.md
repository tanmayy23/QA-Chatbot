Banas Quizmaster

BanasQuizMaster is a real-time, full-stack quiz platform for education and corporate training. Admins create, edit, and manage quizzes via a secure dashboard, while users take quizzes in distraction-free full screen mode with live leaderboards.

Key Features • Role-Based Interfaces: Dedicated dashboards for Admins (quiz creation & management) and Users (taking quizzes & viewing results).

Real-Time Leader board: Live score and rank updates during quizzes using Web Socket (Socket.IO).

Main Functionalities • Quiz Creation & Editing: Admins can create, edit, and

organize quiz content with full control.

Quiz

user-friendly Interface: Responsive, interface supporting multiple question types (e.g., MCQ, true/false).

Taking

Session Persistence: Auto-saves answers and timer progress in local Storage to resume interrupted attempts. JWT-based login/logout with

Secure Authentication:

Result Review: Detailed performance feedback with score breakdown and answer explanations.

Dashboard: Centralized hub for Admins (manage

protected session management.

Full screen Quiz Mode: Distraction-free, mandatory full-

quizzes) and Users (view active quizzes & results). Logs

Attempt

Tracking:

all

quiz

attempts with

screen interface with no navigation back.

timestamps, scores, and performance trends.

This is the main landing page where users first arrive. From here, clicking the login or register button directs them to the login and registration pages and it can be accessed via the address 10.40.0.33:3001.

This is the Login/Register page where employees can securely sign in or create an account (if they are new users) to access the quiz platform.

In this section, the Admin creates new projects by filling in the required fields and using a drag-and-drop feature to upload a text file containing questions and answers, which will automatically populate the quiz questions.

This is the Admin Dashboard, where administrators can create new quizzes, view and manage previously created quizzes.

In this section, the Admin can manage projects they have created. They can archive a project to hide it from all users or stop an active project, immediately preventing further participation in the quiz.

This is the User Dashboard, where participants can view all ongoing quizzes available for participation and join them directly. Users can track real-time leaderboard rankings for each quiz, monitor their personal performance, and review past results.

Remaining Time for Quiz to Auto Submit

This is the Quiz-Taking Interface, where users participate in assessments. It features a real-time dashboard displaying current rankings and performance metrics as participants progress. There is no previous button once a question is answered, it cannot be revisited—and the quiz must be taken in full-screen mode.

This is the Leaderboard Section, where participants can view the rankings of all users based on their quiz performance. The leaderboard highlights top performers across assessments.

This interface appears upon quiz submission, displaying the user’s final score as a percentage. It includes correct/incorrect answer counts