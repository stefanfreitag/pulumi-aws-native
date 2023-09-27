// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class ConnectorProfileServiceNowConnectorProfileCredentialsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The OAuth 2.0 credentials required to authenticate the user.
        /// </summary>
        [Input("oAuth2Credentials")]
        public Input<Inputs.ConnectorProfileOAuth2CredentialsArgs>? OAuth2Credentials { get; set; }

        /// <summary>
        /// The password that corresponds to the username.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// The name of the user.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ConnectorProfileServiceNowConnectorProfileCredentialsArgs()
        {
        }
        public static new ConnectorProfileServiceNowConnectorProfileCredentialsArgs Empty => new ConnectorProfileServiceNowConnectorProfileCredentialsArgs();
    }
}
