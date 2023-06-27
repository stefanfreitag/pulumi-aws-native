// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2.Inputs
{

    public sealed class ListenerAuthenticateCognitoConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("authenticationRequestExtraParams")]
        public Input<object>? AuthenticationRequestExtraParams { get; set; }

        [Input("onUnauthenticatedRequest")]
        public Input<string>? OnUnauthenticatedRequest { get; set; }

        [Input("scope")]
        public Input<string>? Scope { get; set; }

        [Input("sessionCookieName")]
        public Input<string>? SessionCookieName { get; set; }

        [Input("sessionTimeout")]
        public Input<string>? SessionTimeout { get; set; }

        [Input("userPoolArn", required: true)]
        public Input<string> UserPoolArn { get; set; } = null!;

        [Input("userPoolClientId", required: true)]
        public Input<string> UserPoolClientId { get; set; } = null!;

        [Input("userPoolDomain", required: true)]
        public Input<string> UserPoolDomain { get; set; } = null!;

        public ListenerAuthenticateCognitoConfigArgs()
        {
        }
        public static new ListenerAuthenticateCognitoConfigArgs Empty => new ListenerAuthenticateCognitoConfigArgs();
    }
}
