// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EKS
{
    public static class GetAddon
    {
        /// <summary>
        /// Resource Schema for AWS::EKS::Addon
        /// </summary>
        public static Task<GetAddonResult> InvokeAsync(GetAddonArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAddonResult>("aws-native:eks:getAddon", args ?? new GetAddonArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Schema for AWS::EKS::Addon
        /// </summary>
        public static Output<GetAddonResult> Invoke(GetAddonInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAddonResult>("aws-native:eks:getAddon", args ?? new GetAddonInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAddonArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of Addon
        /// </summary>
        [Input("addonName", required: true)]
        public string AddonName { get; set; } = null!;

        /// <summary>
        /// Name of Cluster
        /// </summary>
        [Input("clusterName", required: true)]
        public string ClusterName { get; set; } = null!;

        public GetAddonArgs()
        {
        }
        public static new GetAddonArgs Empty => new GetAddonArgs();
    }

    public sealed class GetAddonInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of Addon
        /// </summary>
        [Input("addonName", required: true)]
        public Input<string> AddonName { get; set; } = null!;

        /// <summary>
        /// Name of Cluster
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        public GetAddonInvokeArgs()
        {
        }
        public static new GetAddonInvokeArgs Empty => new GetAddonInvokeArgs();
    }


    [OutputType]
    public sealed class GetAddonResult
    {
        /// <summary>
        /// Version of Addon
        /// </summary>
        public readonly string? AddonVersion;
        /// <summary>
        /// Amazon Resource Name (ARN) of the add-on
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The configuration values to use with the add-on
        /// </summary>
        public readonly string? ConfigurationValues;
        /// <summary>
        /// IAM role to bind to the add-on's service account
        /// </summary>
        public readonly string? ServiceAccountRoleArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.AddonTag> Tags;

        [OutputConstructor]
        private GetAddonResult(
            string? addonVersion,

            string? arn,

            string? configurationValues,

            string? serviceAccountRoleArn,

            ImmutableArray<Outputs.AddonTag> tags)
        {
            AddonVersion = addonVersion;
            Arn = arn;
            ConfigurationValues = configurationValues;
            ServiceAccountRoleArn = serviceAccountRoleArn;
            Tags = tags;
        }
    }
}
