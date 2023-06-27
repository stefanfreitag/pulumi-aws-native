// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpenSearchServerless.Outputs
{

    /// <summary>
    /// Describes saml options in form of key value map
    /// </summary>
    [OutputType]
    public sealed class SecurityConfigSamlConfigOptions
    {
        /// <summary>
        /// Group attribute for this saml integration
        /// </summary>
        public readonly string? GroupAttribute;
        /// <summary>
        /// The XML saml provider metadata document that you want to use
        /// </summary>
        public readonly string Metadata;
        /// <summary>
        /// Defines the session timeout in minutes
        /// </summary>
        public readonly int? SessionTimeout;
        /// <summary>
        /// Custom attribute for this saml integration
        /// </summary>
        public readonly string? UserAttribute;

        [OutputConstructor]
        private SecurityConfigSamlConfigOptions(
            string? groupAttribute,

            string metadata,

            int? sessionTimeout,

            string? userAttribute)
        {
            GroupAttribute = groupAttribute;
            Metadata = metadata;
            SessionTimeout = sessionTimeout;
            UserAttribute = userAttribute;
        }
    }
}
