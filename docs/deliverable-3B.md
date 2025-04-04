## Sprint 3 Tasks and Results:

### Wade:
- Add game over and game won screens, time limit that causes frog death, improved commenting
 - **Status**: Completed
 - **Branch**: I pushed changes to branches feature/scoring-with-lily-pads and feature/game-over-and-timer.

### Liz:
- Get the frogs to stick to the lilypad and generate a new player sprite. Also losing a life if the current player sprites if it jumps on the lilypad with the frog on it.
 - **Status**: Completed.
 - **Branch**: I pushed changes to the main branch because I was having issues with git.

### David:
- Add upper boundary
- Add left right and bottom boundaries
- organized some of the sprites, images, etc
- **Status**:Completed
 - **Branch**: Used Upper Boundary branch for upper boundary, organization branch for organization, and eventually main for finishing touches so that they would be visible to the whole team right away.

### Zoe:
- Clean up the various screens and make visually aesthetic
- Get top scoring to display in the menu view 
 - **Status**: The screens are completed and all work. The high scoring is implemented, but slightly buggy. The user must press escape to exit the game and clear the csv file containing their high scores. When the file is first empty, the scores sometimes get written multiple times. Overall logic works correctly for maintaing the high scores and displaying them on the menu view. 
 - **Branch**: Pushed changes to the main branch.

Deliverable 3B

Tasks:
- Add game over screen at lives = 0 (easy, essential)
Implemented.  You will see it when you play and your lives hit zero.

- Add timer for frog death/restart (medium, nice to have)
Implemented.  The frog dies when the 60 second timer hits zero.

- Add side screen collisions (easy, essential)
Implemented.  The fromg now dies if he hits left, right, or bottom (with a little wiggle room on the botom for when he goes sideways/changes orientation).

- Improve upper bounds around lily pads (hard, essential)
Implemented.  The frog will now die if he hits the grass at the top of the screen.  Go between to hit the lily pads and be safe.

- Change lily pad color/mark lily pad with frog (medium, essential)
Implemented.  The lily pad are now marked with a frog sprite when full.

- Implement sounds (medium, nice to have) (not currently planned but might be a stretch goal)
Not Implemented.  This was a stretch goal and we decided not to do it.

- Update start screen with full instructions text (easy, important)
Implemented.  When you start the game you will now see clear instuctions on the start screen.

- Blue frog (hard, nice-to-have)
Not Implemented:  Was kind of a stretch goal that never ended up happenning.
- Flies (medium, nice-to-have)
Not Implemented:  Was kind of a stretch goal that never ended up happenning.

- Tidy code: move classes into separate files and all attachments into the assets folder (easy, nice-to-have)
Implemented: Code is all well organized now.

- Comment all functions (easy, nice-to-have)
Implemented:  all functions should now have robust comments and easy readability
