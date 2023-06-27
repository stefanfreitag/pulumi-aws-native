// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecretsManager.Outputs
{

    [OutputType]
    public sealed class SecretGenerateSecretString
    {
        /// <summary>
        /// A string that excludes characters in the generated password. By default, all characters from the included sets can be used. The string can be a minimum length of 0 characters and a maximum length of 7168 characters. 
        /// </summary>
        public readonly string? ExcludeCharacters;
        /// <summary>
        /// Specifies the generated password should not include lowercase letters. By default, ecrets Manager disables this parameter, and the generated password can include lowercase False, and the generated password can include lowercase letters.
        /// </summary>
        public readonly bool? ExcludeLowercase;
        /// <summary>
        /// Specifies that the generated password should exclude digits. By default, Secrets Manager does not enable the parameter, False, and the generated password can include digits.
        /// </summary>
        public readonly bool? ExcludeNumbers;
        /// <summary>
        /// Specifies that the generated password should not include punctuation characters. The default if you do not include this switch parameter is that punctuation characters can be included. 
        /// </summary>
        public readonly bool? ExcludePunctuation;
        /// <summary>
        /// Specifies that the generated password should not include uppercase letters. The default behavior is False, and the generated password can include uppercase letters. 
        /// </summary>
        public readonly bool? ExcludeUppercase;
        /// <summary>
        /// The JSON key name used to add the generated password to the JSON structure specified by the SecretStringTemplate parameter. If you specify this parameter, then you must also specify SecretStringTemplate. 
        /// </summary>
        public readonly string? GenerateStringKey;
        /// <summary>
        /// Specifies that the generated password can include the space character. By default, Secrets Manager disables this parameter, and the generated password doesn't include space
        /// </summary>
        public readonly bool? IncludeSpace;
        /// <summary>
        /// The desired length of the generated password. The default value if you do not include this parameter is 32 characters. 
        /// </summary>
        public readonly int? PasswordLength;
        /// <summary>
        /// Specifies whether the generated password must include at least one of every allowed character type. By default, Secrets Manager enables this parameter, and the generated password includes at least one of every character type.
        /// </summary>
        public readonly bool? RequireEachIncludedType;
        /// <summary>
        /// A properly structured JSON string that the generated password can be added to. If you specify this parameter, then you must also specify GenerateStringKey.
        /// </summary>
        public readonly string? SecretStringTemplate;

        [OutputConstructor]
        private SecretGenerateSecretString(
            string? excludeCharacters,

            bool? excludeLowercase,

            bool? excludeNumbers,

            bool? excludePunctuation,

            bool? excludeUppercase,

            string? generateStringKey,

            bool? includeSpace,

            int? passwordLength,

            bool? requireEachIncludedType,

            string? secretStringTemplate)
        {
            ExcludeCharacters = excludeCharacters;
            ExcludeLowercase = excludeLowercase;
            ExcludeNumbers = excludeNumbers;
            ExcludePunctuation = excludePunctuation;
            ExcludeUppercase = excludeUppercase;
            GenerateStringKey = generateStringKey;
            IncludeSpace = includeSpace;
            PasswordLength = passwordLength;
            RequireEachIncludedType = requireEachIncludedType;
            SecretStringTemplate = secretStringTemplate;
        }
    }
}
