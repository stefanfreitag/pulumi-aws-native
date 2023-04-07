// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner.Outputs
{

    /// <summary>
    /// Authentication Configuration
    /// </summary>
    [OutputType]
    public sealed class ServiceAuthenticationConfiguration
    {
        /// <summary>
        /// Access Role Arn
        /// </summary>
        public readonly string? AccessRoleArn;
        /// <summary>
        /// Connection Arn
        /// </summary>
        public readonly string? ConnectionArn;

        [OutputConstructor]
        private ServiceAuthenticationConfiguration(
            string? accessRoleArn,

            string? connectionArn)
        {
            AccessRoleArn = accessRoleArn;
            ConnectionArn = connectionArn;
        }
    }
}
