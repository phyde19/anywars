# AnyWars Implementation Plan

## 1. Difficulty Levels (Kyu System)

**8 kyu**: Absolute beginner. Focuses on basic syntax and simple concepts.
**7 kyu**: Beginner. Introduction to common patterns and slightly more complex concepts.
**6 kyu**: Novice. Combines multiple concepts, requires more thought.
**5 kyu**: Competent. Requires understanding of domain-specific knowledge and problem-solving.
**4 kyu**: Proficient. Complex problems requiring deep understanding of concepts.
**3 kyu**: Advanced. Challenging problems requiring creative solutions.
**2 kyu**: Expert. Very difficult problems pushing the boundaries of the domain.
**1 kyu**: Master. Extremely difficult problems requiring exceptional expertise.

## 2. Core Components

### Challenge Generation

For each challenge, Claude will provide:
- Title and description
- Problem statement with requirements
- Input/output examples
- Initial visible test cases
- Hidden test cases (not revealed until submission)
- Context/background knowledge required
- Learning objectives

### Test Framework

Two-tier testing approach:
1. **Visible Tests**: Simple examples provided with the challenge
2. **Hidden Tests**: More comprehensive tests including edge cases

### Solution Verification

When a solution is submitted:
1. Run against visible tests first (for quick feedback)
2. If passed, run against hidden tests
3. Only mark as complete if all tests pass

### Solution Showcase

After successfully completing a challenge:
1. Best practice solution (focusing on readability, maintainability)
2. Clever solution (focusing on performance, elegant approaches)
3. Explanation of each solution approach
4. Discussion of trade-offs between different approaches

## 3. Workflow Protocol

### Starting a New Challenge

When starting a new challenge:
1. Generate an appropriate challenge at the requested difficulty level
2. Save challenge to a markdown file with visible tests
3. Create a hidden test file (which Claude knows but isn't shared)

This can be requested in natural language, specifying domain and difficulty level.

### Working on a Challenge

Files structure:
```
challenges/
  [challenge-name]/
    README.md      # Challenge description and visible tests
    solution.[ext] # Your solution file
    tests.js       # Test runner (visible tests only)
    .hidden/       # Hidden tests (conceptual - Claude maintains this)
```

### Running Tests

When testing a solution:
1. Run your solution against visible tests
2. Provide detailed feedback on failing tests

This can be requested in natural language, referring to the challenge.

### Submitting a Solution

When submitting a solution:
1. Run your solution against all tests (visible and hidden)
2. If all tests pass:
   - Mark challenge as complete
   - Show solution showcase
3. If any tests fail:
   - Show which tests failed
   - Provide hints without revealing solutions

This can be requested in natural language when you're ready to submit.

### Viewing Solutions

When viewing solutions:
1. Check if you've completed the challenge
2. If completed:
   - Show best practice solution
   - Show clever solution
   - Provide explanations
3. If not completed:
   - Remind you to solve it first
   - Offer hints if requested

This can be requested in natural language after completing a challenge.

## 4. Implementation Steps

1. Set up directory structure in `anywars/`
2. Create sample challenges for different domains and difficulty levels
3. Use Claude to maintain the state of challenges (completed/incomplete)
4. Define domain-specific test frameworks as needed

## 5. Domain Examples

AnyWars can be extended to many technical domains:

- **Web Development**: Frontend components, API implementations, etc.
- **DevOps**: Infrastructure as code, CI/CD pipelines, etc.
- **Database Design**: Schema creation, query optimization, etc.
- **Machine Learning**: Feature engineering, model selection, etc.
- **System Design**: Designing scalable architectures
- **Security**: Identifying and fixing vulnerabilities

## 6. Getting Started

To begin using AnyWars:

1. Choose a domain you want to improve in
2. Start with an appropriate kyu level
3. Request a challenge with `new-challenge`
4. Work on your solution independently
5. Test with `test-solution` to get feedback
6. Submit with `submit-solution` when ready
7. Learn from better solutions with `show-solutions`