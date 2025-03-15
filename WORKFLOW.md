# AnyWars Challenge Workflow

This document details the complete workflow for creating, solving, testing, and reviewing challenges in the AnyWars system, similar to Codewars but for any technical domain. These instructions are comprehensive enough to recover if conversation context is lost.

## Project Structure

```
anywars/
├── README.md                 # Project overview
├── WORKFLOW.md               # This file - detailed workflow
├── domains.md                # List of available domains
└── domains/                  # Domain directories
    └── [domain_name]/        # e.g., shell_scripting
        ├── README.md         # Domain description
        ├── 8_kyu/            # Easy challenges
        │   └── [challenge]/  # Individual challenge
        │       ├── README.md           # Challenge description
        │       ├── [starter_file]      # Template to start with
        │       ├── test_visible.sh     # Visible tests
        │       └── test_hidden.sh      # Hidden tests
        ├── 7_kyu/            # And so on for each difficulty level
        └── ... 
```

## Detailed Workflow Instructions

### Creating a New Domain

1. **Request a new domain**:
   ```
   "I'd like to create a new domain for [domain_name] challenges"
   ```

2. **Claude will**:
   - Check if the domain already exists
   - If not, create the domain directory: `/domains/[domain_name]/`
   - Create the domain README with detailed description
   - Create kyu level directories (8_kyu through 1_kyu)
   - Update the domains.md file with the new domain
   - Respond with confirmation

### Requesting a Challenge

1. **Request a challenge in a specific domain and difficulty**:
   ```
   "I'd like a [domain_name] challenge at [kyu_level] level"
   ```

2. **Claude will**:
   - Check if the domain exists (if not, offer to create it)
   - Create a new challenge with a descriptive name
   - Create the challenge directory with:
     - README.md (description)
     - Starter file (minimal template)
     - test_visible.sh (basic tests)
     - test_hidden.sh (comprehensive tests)
   - Make test files executable
   - Respond with the challenge description

### Working on a Challenge

1. **Start solving**:
   ```
   "I'll start working on this challenge"
   ```

2. **Edit your solution**:
   ```
   "Here's my solution: [your code]"
   ```
   or
   ```
   "Edit the solution file with [your code]"
   ```

3. **Run visible tests**:
   ```
   "Let's test my solution with the visible tests"
   ```

4. **Submit final solution**:
   ```
   "I'm ready to submit my final solution"
   ```

5. **View model solutions** (only after passing all tests):
   ```
   "Show me the model solutions"
   ```

### Recovery Instructions

If conversation context is lost, you can use these commands to recover:

1. **List available domains**:
   ```
   "Show me the available domains in AnyWars"
   ```

2. **List challenges in a domain**:
   ```
   "List all challenges in the [domain_name] domain"
   ```

3. **Continue working on a specific challenge**:
   ```
   "I want to continue working on the [challenge_name] challenge in [domain_name]"
   ```

## Challenge Creation Guidelines

When creating challenges, Claude will follow these principles:

1. **Difficulty Levels**:
   - 8 kyu: Beginner-friendly, basic concepts
   - 7 kyu: Introduces slightly more complex concepts
   - 6 kyu: Requires combining multiple concepts
   - 5 kyu: Requires domain knowledge and problem-solving
   - 4 kyu: Complex problems requiring deeper understanding
   - 3 kyu: Advanced challenges requiring creative solutions
   - 2 kyu: Very difficult problems for experts
   - 1 kyu: Extremely difficult, mastery-level challenges

2. **Challenge Components**:
   - Clear description and requirements
   - Input/output examples
   - Visible test cases
   - Hidden test cases for edge conditions
   - Minimal starter file
   - Expected skills and learning outcomes

3. **Domain-Specific Considerations**:
   - Each domain has its own focus areas and tooling
   - Tests are adapted to the specific domain
   - Challenges should represent real-world scenarios

## Testing Protocol

1. **Visible Tests**:
   - Basic test cases shown in the challenge description
   - Provides immediate feedback during development
   - Runs with `./test_visible.sh`

2. **Hidden Tests**:
   - More comprehensive test suite including edge cases
   - Only shown after submission
   - Tests for error handling, performance, etc.
   - Runs with `./test_hidden.sh`

3. **Model Solutions**:
   - Only shown after passing all tests
   - Includes "best practice" solution (readable, maintainable)
   - Includes "clever" solution (efficient, elegant)
   - Explanations of approaches and trade-offs