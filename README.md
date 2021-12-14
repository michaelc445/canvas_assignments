# canvas_assignments
Retrieves assignments from canvas and displays due dates aswell as some other information on the assignment.


First go to your canvas profile -> settings -> new access token and add this token to the token in get_assignment_for_course
You'll need to edit the courses dictionary and add your modules. "Module name":course_id. 
the course_id is available in the url for each module page. eg "https://ucc.instructure.com/courses/<course_id>"
also need to change the url in get_assignment_for_course to match the url for your college's canvas api
