// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Outputs
{

    [OutputType]
    public sealed class ConnectorProfileMarketoConnectorProfileCredentials
    {
        /// <summary>
        /// The credentials used to access protected resources.
        /// </summary>
        public readonly string? AccessToken;
        /// <summary>
        /// The identiﬁer for the desired client.
        /// </summary>
        public readonly string ClientId;
        /// <summary>
        /// The client secret used by the oauth client to authenticate to the authorization server.
        /// </summary>
        public readonly string ClientSecret;
        /// <summary>
        /// The oauth needed to request security tokens from the connector endpoint.
        /// </summary>
        public readonly Outputs.ConnectorProfileConnectorOAuthRequest? ConnectorOAuthRequest;

        [OutputConstructor]
        private ConnectorProfileMarketoConnectorProfileCredentials(
            string? accessToken,

            string clientId,

            string clientSecret,

            Outputs.ConnectorProfileConnectorOAuthRequest? connectorOAuthRequest)
        {
            AccessToken = accessToken;
            ClientId = clientId;
            ClientSecret = clientSecret;
            ConnectorOAuthRequest = connectorOAuthRequest;
        }
    }
}
