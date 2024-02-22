// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Eks
{
    public static class GetIdentityProviderConfig
    {
        /// <summary>
        /// An object representing an Amazon EKS IdentityProviderConfig.
        /// </summary>
        public static Task<GetIdentityProviderConfigResult> InvokeAsync(GetIdentityProviderConfigArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIdentityProviderConfigResult>("aws-native:eks:getIdentityProviderConfig", args ?? new GetIdentityProviderConfigArgs(), options.WithDefaults());

        /// <summary>
        /// An object representing an Amazon EKS IdentityProviderConfig.
        /// </summary>
        public static Output<GetIdentityProviderConfigResult> Invoke(GetIdentityProviderConfigInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIdentityProviderConfigResult>("aws-native:eks:getIdentityProviderConfig", args ?? new GetIdentityProviderConfigInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIdentityProviderConfigArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the identity provider configuration.
        /// </summary>
        [Input("clusterName", required: true)]
        public string ClusterName { get; set; } = null!;

        /// <summary>
        /// The name of the OIDC provider configuration.
        /// </summary>
        [Input("identityProviderConfigName", required: true)]
        public string IdentityProviderConfigName { get; set; } = null!;

        /// <summary>
        /// The type of the identity provider configuration.
        /// </summary>
        [Input("type", required: true)]
        public Pulumi.AwsNative.Eks.IdentityProviderConfigType Type { get; set; }

        public GetIdentityProviderConfigArgs()
        {
        }
        public static new GetIdentityProviderConfigArgs Empty => new GetIdentityProviderConfigArgs();
    }

    public sealed class GetIdentityProviderConfigInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the identity provider configuration.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        /// <summary>
        /// The name of the OIDC provider configuration.
        /// </summary>
        [Input("identityProviderConfigName", required: true)]
        public Input<string> IdentityProviderConfigName { get; set; } = null!;

        /// <summary>
        /// The type of the identity provider configuration.
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.Eks.IdentityProviderConfigType> Type { get; set; } = null!;

        public GetIdentityProviderConfigInvokeArgs()
        {
        }
        public static new GetIdentityProviderConfigInvokeArgs Empty => new GetIdentityProviderConfigInvokeArgs();
    }


    [OutputType]
    public sealed class GetIdentityProviderConfigResult
    {
        /// <summary>
        /// The ARN of the configuration.
        /// </summary>
        public readonly string? IdentityProviderConfigArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetIdentityProviderConfigResult(
            string? identityProviderConfigArn,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            IdentityProviderConfigArn = identityProviderConfigArn;
            Tags = tags;
        }
    }
}
