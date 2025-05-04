class PasswordSuggester:
    
    def suggest_passwords(self, answers: dict, num_passwords=5) -> list:
        prompt = self._build_prompt(answers, num_passwords)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a password security expert."},
                    {"role": "user", "content": prompt}
                ],
                stream=False
            )

            raw_output = response.choices[0].message.content.strip()
            return self._parse_passwords(raw_output)

        except Exception as e:
            return [f"[ERROR] Failed to generate passwords: {str(e)}"]

    def _build_prompt(self, answers: dict, num_passwords: int) -> str:
        prompt_lines = [
            f"Generate {num_passwords} strong password suggestions based on the following personal inputs:"
        ]

        for i in range(1, 11):
            answer = answers.get(f"question_{i}", "").strip()
            if answer:
                prompt_lines.append(f"Q{i}: {answer}")

# It is a critical part of the instructions (prompt) that guides the model to generate strong and correct passwords according to security standards
        prompt_lines.append("""
Passwords must follow these rules:
- Minimum length: 12 characters
- Must include: uppercase letters, lowercase letters, numbers, and special characters
- Should be memorable yet secure
- DO NOT explain, just list the passwords only, each on a new line
        """)

        return "\n".join(prompt_lines)

    def _parse_passwords(self, raw_output: str) -> list:
        lines = raw_output.splitlines()
        passwords = [line.strip("0123456789. ").strip() for line in lines if line.strip() and len(line.strip()) >= 12]
        return passwords[:5]

