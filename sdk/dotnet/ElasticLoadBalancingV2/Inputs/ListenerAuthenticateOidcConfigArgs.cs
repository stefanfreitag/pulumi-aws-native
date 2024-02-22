// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2.Inputs
{

    public sealed class ListenerAuthenticateOidcConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("authenticationRequestExtraParams")]
        private InputMap<string>? _authenticationRequestExtraParams;
        public InputMap<string> AuthenticationRequestExtraParams
        {
            get => _authenticationRequestExtraParams ?? (_authenticationRequestExtraParams = new InputMap<string>());
            set => _authenticationRequestExtraParams = value;
        }

        [Input("authorizationEndpoint", required: true)]
        public Input<string> AuthorizationEndpoint { get; set; } = null!;

        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("clientSecret")]
        public Input<string>? ClientSecret { get; set; }

        [Input("issuer", required: true)]
        public Input<string> Issuer { get; set; } = null!;

        [Input("onUnauthenticatedRequest")]
        public Input<string>? OnUnauthenticatedRequest { get; set; }

        [Input("scope")]
        public Input<string>? Scope { get; set; }

        [Input("sessionCookieName")]
        public Input<string>? SessionCookieName { get; set; }

        [Input("sessionTimeout")]
        public Input<string>? SessionTimeout { get; set; }

        [Input("tokenEndpoint", required: true)]
        public Input<string> TokenEndpoint { get; set; } = null!;

        [Input("useExistingClientSecret")]
        public Input<bool>? UseExistingClientSecret { get; set; }

        [Input("userInfoEndpoint", required: true)]
        public Input<string> UserInfoEndpoint { get; set; } = null!;

        public ListenerAuthenticateOidcConfigArgs()
        {
        }
        public static new ListenerAuthenticateOidcConfigArgs Empty => new ListenerAuthenticateOidcConfigArgs();
    }
}
