def minimal_courses(weights, max_weight):
    weights.sort(reverse=True)

    courses = []

    for weight in weights:
        added = False

        for course in courses:
            if sum(course) + weight <= max_weight:
                course.append(weight)
                added = True
                break

        if not added:
            courses.append([weight])

    return len(courses), courses

weights = [10,8,7,4,5,10,12,3]
max_weight = 15

num_courses, courses = minimal_courses(weights, max_weight)
print(num_courses,courses)