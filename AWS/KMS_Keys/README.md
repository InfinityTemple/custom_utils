### Updated README.md

# KMS Key Grants Examiner

## Description
The KMS Key Grants Examiner is a Python tool designed to list all KMS Key grants for a given AWS account. It provides additional information that can help establish whether the key grants are still relevant, such as the last used date, which assists cloud engineers in adhering to the Least Privilege principle by identifying and removing outdated and irrelevant permissions.

## Prerequisites
Before running the KMS Key Grants Examiner, ensure you have the following prerequisites:
1. **Python 3.x**: Make sure Python 3.x is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
2. **AWS CLI**: The AWS Command Line Interface (CLI) should be installed and configured with the necessary permissions to access KMS keys and grants. You can install it from [AWS CLI official website](https://aws.amazon.com/cli/).
3. **Boto3**: The Boto3 library for Python should be installed. Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2.

## Installation
Follow these steps to install and set up the KMS Key Grants Examiner:

1. **Clone the repository** (or download the script):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python packages**:
   ```bash
   pip install boto3
   ```

## Configuration
1. **Configure AWS CLI**:
   Ensure the AWS CLI is configured with the necessary credentials and region. You can configure it using the following command:
   ```bash
   aws configure
   ```
   You will be prompted to enter your AWS Access Key ID, Secret Access Key, default region, and default output format.

## Usage
To use the KMS Key Grants Examiner, run the script as follows:

1. **Run the script**:
   ```bash
   python kms_grants_examiner.py
   ```

2. **Enter AWS Credentials**:
   You will be prompted to enter your AWS credentials:
   - AWS Access Key ID
   - AWS Secret Access Key
   - AWS Session Token (if applicable)
   - AWS Region (default: us-west-1)

3. **Output**:
   The script will output detailed information for each KMS key grant, including:
   - `KeyId`: The unique identifier for the KMS key.
   - `GrantId`: The unique identifier for the grant.
   - `GrantName`: The name of the grant, if provided.
   - `GranteePrincipal`: The principal (IAM entity) to which the grant is issued.
   - `CreationDate`: The date when the grant was created.
   - `LastUsedDate`: The date when the grant was last used, if available.

## Example Output
Here is an example of what the output might look like:
```plaintext
KeyId: 1234abcd-12ab-34cd-56ef-1234567890ab, GrantId: 5678efgh-12ef-34gh-56ij-7890123456kl, GrantName: example-grant, GranteePrincipal: arn:aws:iam::123456789012:user/example-user, CreationDate: 2023-01-01T12:00:00Z, LastUsedDate: 2023-05-01T12:00:00Z
KeyId: abcd1234-34cd-12ab-56ef-abcdef123456, GrantId: efgh5678-34gh-12ef-56ij-1234567890kl, GrantName: another-grant, GranteePrincipal: arn:aws:iam::123456789012:role/example-role, CreationDate: 2022-07-15T08:00:00Z, LastUsedDate: 2023-04-20T08:00:00Z
```

## Detailed Steps
1. **Install Python**:
   - Download and install Python from [Python's official website](https://www.python.org/downloads/).
   - Verify the installation:
     ```bash
     python --version
     ```

2. **Install AWS CLI**:
   - Follow the installation instructions on [AWS CLI official website](https://aws.amazon.com/cli/).
   - Verify the installation:
     ```bash
     aws --version
     ```

3. **Configure AWS CLI**:
   - Configure your AWS credentials and region:
     ```bash
     aws configure
     ```

4. **Install Boto3**:
   - Use pip to install Boto3:
     ```bash
     pip install boto3
     ```

5. **Run the KMS Key Grants Examiner Script**:
   - Clone the repository and navigate to the directory:
     ```bash
     git clone <repository-url>
     cd <repository-directory>
     ```
   - Run the script:
     ```bash
     python kms_grants_examiner.py
     ```
   - Enter your AWS credentials when prompted.

## Troubleshooting
- **Missing AWS Credentials**: Ensure that the AWS CLI is properly configured with `aws configure`.
- **Permissions Error**: Make sure your AWS IAM user or role has the necessary permissions to list KMS keys and grants.
- **Dependencies Issues**: Ensure all required Python packages are installed using `pip install boto3`.

## Additional Information
- **AWS KMS Documentation**: For more information on AWS KMS, visit the [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/).
- **Boto3 Documentation**: For detailed Boto3 documentation, visit the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact
For any issues or inquiries, please contact [your-email@example.com].
```

This updated script now prompts for the AWS credentials using `input` instead of `getpass` and includes the AWS region with a default of `us-west-1`. The `README.md` has also been updated to reflect these changes.