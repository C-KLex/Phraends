# Project Development Guideline

## **📛Naming Convention Guide**

- Folder: Snake_Case (Uppercase Initial), **Exceptions: `templates` folder for Flask Project**
- Files: Snake_Case (Uppercase Initial)
- Class: Snake_Case (Uppercase Initial)
- Function: snake_case
- Variables: snake_case
- Dates: YYYYMMDD
- Versions: xxx001, xxx002

---

## **🎨Coding Style Guide**

### General Guideline

#### Script Structure

```python
# Import the external package first
import numpy as np
import pandas as pd

# Import ther internal package
from A import a
from B import b 

class foo1:

    # Return type example
    def bar1(var1: int, var2: str) -> int():

        # some code
        some_code()

        return 3

    # No return type example
    def bar2(var1: str, var2: str):
        
        # some code
        some_code()

        return

if __name__ == "__main__":

    # some code

```

Key Point

1. Script Structure & Order

    - Import internal package (package built by developers)

    - Import external package, e.g `numpy`, `random`

    - Main code

    - Run section (if available)

2. Function Guideline

    - Parameter Type: Write down the input parameter data type

    - Return Type: Write down the return data type, **except return nothing**.

    - Always Return: Write down `return` even if it returns nothing

#### Whitespace

1. No whitespace:

    - inside parentheses, brackets, braces  (), [], {}

        ```python
        # right
        def function1(var1, var2)
        # wrong
        def function1( var1, var2 )
        ```

    - before a comma, semicolon, colon  , ; :

        ```python
        # right
        def function1(var1, var2)
        # wrong
        def function1(var1,var2)
        ```

    - before a open parenthese, bracket, brace which is a start of a function call

        ```python
        # right
        def function1(var1, var2)
        # wrong
        def function1 (var1, var2)
        ```

2. One whitespace around:

    - an assignment operater

        ```python
        # right
        var1 = 0
        # wrong
        var1=0
        var1 =0
        var1= 0
        ```

    - reserved word starting a conditional statement with parentheses

        ```python
        # right
        if (x>1 & x<2):
        # wrong
        if(x>1 & x<2):
        ```

    - braces if follows codes in the same line

#### Vertical Whitespace

1. A single blank line appears when separating the logic of codes

    ```python
    def function1():
        print("yoo")
        print("same funtion")
    # 1st blank line
    def function2():
        print("this is another function")
    ```

2. Multiple blank lines are permitted, but never required (nor encouraged). e.g. blanks between class

    ```python
    class Class1:
        def __init__(self):
            print("this is initial function")
        
        def function1():
            print("this is function1 from class1")
    # 1st blank line
    # 2nd blank line
    class Class2:
        def __init__(self):
            print("this is initial function")
        
        def function2():
            print("this is function2 from class2")
    ```

#### Parentheses

1. Parentheses are not used around the top-most expression that follows an conditional statement

    ```python
    # right
    if x = 1:
    # wrong
    if (x = 1):
    ```

### Specific Guideline

#### Properties

1. Use meaningful names for your properties that accurately describe their purpose. Follow the naming convention recommended by PEP8, which suggest using lowercase letters and underscores for property names (my_property instead of myProperty)

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

        @property
        def my_property(self):
            return self._my_property
    ```

2. In Python, properties are often implemented using the @property decorator. Place this decorator above the getter method to indicate that the method is accessed as a property rather than a regular method.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

        @property
        def my_property(self):
            return self._my_property
    ```

3. Keep the naming consistent for the underlying private attribute associated with the property. Prefix it with an underscore (_) to indicate that it's intended to be private. This convention helps differentiate the property from the attribute itself.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None
            
        @property
        def my_property(self):
            return self._my_property
    ```

4. If you want to allow setting the value of the property, define a setter method using the @property_name.setter decorator.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

            @property
            def my_property(self):
                return self._my_property

        @my_property.setter
        def my_property(self, value):
            # Property setter logic
            self._my_property = value
    ```

5. If a property should be read-only, define only the getter method and omit the setter method.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

        @property
        def my_property(self):
            return self._my_property
        ```

#### Switch Statements

1. Indent the body of the switch statement to improve readability. Use either a tab or four spaces or a tab for indentation.

2. Start each case label on a new line and indent it one level deeper than the switch statement. Align the case labels vertically for better readability. Additionally, use braces {} for all cases, even if they're not strictly necessary.

    ```python
    switch variable:
        case value1:
            {
                # code for value1
                break
            }
        case value2:
            {
                # code for value2
                break
            }
        case value3:
            {
                # code for value3
                break
            }
        default:
            {
                # code for all other cases
            }
    ```

3. Always include a default case to handle unexpected values. This case should clearly communicate how unexpected values are handled.

4. Include a break statement at the end of each case to prevent fall-through to the next case. If fall-through is intentional, document it with a comment.

---

## **📄Documentation Guide**

### 👋Full Script Example

```python
"""
Summary:
    Write the introduction for the script.

Description: 
    Write more detail if needed. 
"""
from A import package_a
from B import package_b

class Example_Class:
    """
    Summary: 
        Some introduction for the class
    
    Description:
        Write more detail if needed.
    """

    def method1(a, b):
        """
        Summary: 
            Introduction for method1
        
        Description:
            Write more detail if needed. 
        
        Warnings:
            Write some warning if needed.
        
        Args:
            a (type): Description of a
            b (type): Description of b 
        
        Returns:
            c (type): Description of c
            d (type): Description of d

        """

        # do something
        do_something()

        # do more 
        do_more()

        return c, d
    
    
if __name__ == '__main__':

    # run a
    a()

    # run b 
    b()

    # run c
    c()

    # end
    end()
```

### 🔑Key Point

- `""" """` Comment

  - Recommendation Keywords

    **Summary, Description, Warnings, Args, Returns**

  - Blank Policy

    **ZERO** blank line above, and **ONE** blank line below.

- `#` Comment

  - As Short As Possible

    A readable code should not need any comments to explain.

  - Blank Policy

    **ONE** blank line above, and **ZERO** blank line below.

---

## **🦮Git Guide**

### 💬Git Commit

- Commit Message

    ```bash
    git commit -m "label: this is a commit summary" -m "this is a commit description (optional)"
    ```

  - Commit Message Style: **all lowercase letters**

  - Label Reference:

    ![image](https://github.com/C-KLex/GitEducation/assets/87312700/e1965358-a970-4116-a260-86d98150ce26)

  - Reference: <https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/>

- Commit Principle: More Commits but Tiny Changes.

    Each commit should represent a specific little change. Don't add too many changes in only one commit because it will make the commit FAT, making it harder to track the history.

### 🌲Branch Naming

- General Branch Naming:

    ```bash
    git branch name/whatYouWantToDo
    git branch kyle/addNewButton
    ```

- Branch Name Style: `name` in lowercase, `whatYouWantToDO` in camelCase

    ```bash
    git branch lowercase/camelCase
    ```

### 🦮Pull Request Principal

- Clear Task

    One PR is only for one task, don't mix multiple tasks into one PR, which will make reviewers hard to review and hard to trace back. For example, let's say PR1 is about `Adding Login Button` and PR1 also contains the changes about `Connecting Login Button with Backend`; then, PR1 is not simple anymore due to the mixture of multiple tasks.

- Small PR

    Some tasks can be enormous, meaning that a lot of code changes would be done at the same time. In this case, it's better to separate the tasks into pieces and PR each of them individually. For example, I need to do a `login module`. I can't simply finish all the code and make it into a single PR, it would be very hard to review. Therefore, I decompose the main tasks into `login page UI`, `login page UX link`, and `login page backend`. Then, I PR one small progress every time I've done a feature.

- Fix Conflict

    Before opening the PR, always check the potential merge conflict first. For example, I want to PR `feature` branch into `main` branch. Before opening the PR, I should always merge `main` into `feature` to see if there is any conflict existing, and if so, I should solve the conflict carefully without ruining other's work from `main`. Therefore, a good merge conflict-solving skill is required, and it takes experience to ace the skill!

### 📜Pull Request Template

- Title, Summary, Detail, Screenshots

    These four components are useful in a PR Report. They are all optional, and you can add more or decide not to use any. For example, you may not be able to provide screenshots in some cases.

- Example: <https://github.com/C-KLex/GymBro/pull/18>

    ![image](https://github.com/C-KLex/GitEducation/assets/87312700/08cee987-dbf1-41e6-9c28-860ed20dd6b6)

### 🌊Git Reminder

Here are some key tips to have a better git experience.

- Know Which Branch You Are In

- Know Which Branch You Want To Merge In

- Know How to Solver Merge Conflict Carefully

- Understand How Much Your Work

- Know When to Stop to Create a Commit

- Know When Should Touch the Main and When Shouldn't
