**What is git conflict**
A git conflict is when two people or two branches changes the same part of a file differently, and Git doesn't know which change to keep

**Steps to resolve git conflict**
Step 1: Identify that a conflict has happened
The first thing is recognizing that there is a conflict. Git will clearly tell you that it was not able to merge automatically and that there is a conflict in a specific file. This usually happens after trying to merge branches or pull changes. At this point, the process pauses because Git needs you to decide what to do next.

Step 2: Find which file has the conflict
Git will mention the name of the file that has the issue. You need to carefully check that file. The conflict is usually in the exact part where two different changes were made to the same section of the file.

Step 3: Open the file and examine the problem
When you open the file, you will see that Git has marked the conflicting area. It shows your version of the changes and the other branch’s version separately. This is Git’s way of asking you to choose which version should stay.

Step 4: Decide how to resolve it
Now you read both versions and think carefully. You can choose to keep your version, keep the other person’s version, or combine both changes into one improved version. The goal is to make sure the final result makes sense and does not remove important information.

Step 5: Remove the conflict markers and clean the file
After deciding what to keep, you delete the conflict indicators that Git added. The file should look normal again, with only the final version of the content remaining.

Step 6: Mark the conflict as resolved
Once you are done editing and saving the file, you tell Git that the issue has been fixed. This lets Git know that the conflict has been handled.

Step 7: Complete the merge
Finally, you finish the process by committing the changes. This creates a new commit that confirms the conflict has been resolved and the branches are now successfully merged.
