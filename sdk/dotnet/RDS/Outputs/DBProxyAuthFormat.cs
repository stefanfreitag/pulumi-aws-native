// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS.Outputs
{

    [OutputType]
    public sealed class DBProxyAuthFormat
    {
        /// <summary>
        /// The type of authentication that the proxy uses for connections from the proxy to the underlying database. 
        /// </summary>
        public readonly Pulumi.AwsNative.RDS.DBProxyAuthFormatAuthScheme? AuthScheme;
        /// <summary>
        /// The type of authentication the proxy uses for connections from clients.
        /// </summary>
        public readonly Pulumi.AwsNative.RDS.DBProxyAuthFormatClientPasswordAuthType? ClientPasswordAuthType;
        /// <summary>
        /// A user-specified description about the authentication used by a proxy to log in as a specific database user. 
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Whether to require or disallow Amazon Web Services Identity and Access Management (IAM) authentication for connections to the proxy. The ENABLED value is valid only for proxies with RDS for Microsoft SQL Server.
        /// </summary>
        public readonly Pulumi.AwsNative.RDS.DBProxyAuthFormatIAMAuth? IAMAuth;
        /// <summary>
        /// The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager. 
        /// </summary>
        public readonly string? SecretArn;

        [OutputConstructor]
        private DBProxyAuthFormat(
            Pulumi.AwsNative.RDS.DBProxyAuthFormatAuthScheme? authScheme,

            Pulumi.AwsNative.RDS.DBProxyAuthFormatClientPasswordAuthType? clientPasswordAuthType,

            string? description,

            Pulumi.AwsNative.RDS.DBProxyAuthFormatIAMAuth? iAMAuth,

            string? secretArn)
        {
            AuthScheme = authScheme;
            ClientPasswordAuthType = clientPasswordAuthType;
            Description = description;
            IAMAuth = iAMAuth;
            SecretArn = secretArn;
        }
    }
}
