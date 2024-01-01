# Project WIZARD: Registration Console Wizard

## Overview
Project WIZARD is a console-based application designed to streamline the registration process by guiding users through a series of phases to collect specific details. The wizard features an engaging Splash Screen, intuitive navigation, and a visually appealing tabular summary of all entered details.

## Features
Splash Screen: A welcoming page with a Start button initiates the wizard phases.

### Phases:
- Phase 1: Enter full name, email, and birth date.
- Phase 2: Provide city, address, and contact number.
- Phase 3: Share social media details and hobbies. The system allows users to navigate between previous and next phases.
- Phase 4: Complete the health phase by answering yes/no questions.

## Navigation:
A menu at the start with options to "Start New" or "Continue."
If 'Start New,' display user details from Phase 1 and enable user inputs.
On each phase, provide 'Next' and 'Prev' options for seamless navigation, along with the option to update fields.
If 'Continue,' prompt the user for the phase level number and navigate accordingly.

### Reset Button:
A 'Reset' button that clears all entered details and redirects the user to the beginning.

## Rules:
- You cannot proceed to a phase without completing the previous one.
- You can go back to a previous phase.
- You cannot change a field that does not exist in the current phase.
- If you want to continue from a specific phase but the previous phases haven't been completed, land on the last completed phase.

## Styling:
Using coloring and other visually appealing elements to enhance the terminal interface.

## Usage
Run the application.
Choose between starting a new registration or continuing from a specific phase.
Follow the wizard phases, entering the required details.
Utilize 'Next' and 'Prev' options for navigation.
Enjoy a tabular summary of all details upon completion.

## Notes
For a fresh start, use the 'Reset' button to clear all information and return to the beginning.
Ensure completion of each phase before progressing to the next.

## Contribution
Contributions to enhance features, improve styling, or fix issues are welcome. Please follow standard coding practices and submit a pull request.

Let the magic of Project WIZARD registration simplify your user onboarding process!




