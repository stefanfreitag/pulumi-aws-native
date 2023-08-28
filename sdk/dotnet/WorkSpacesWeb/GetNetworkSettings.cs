// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb
{
    public static class GetNetworkSettings
    {
        /// <summary>
        /// Definition of AWS::WorkSpacesWeb::NetworkSettings Resource Type
        /// </summary>
        public static Task<GetNetworkSettingsResult> InvokeAsync(GetNetworkSettingsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNetworkSettingsResult>("aws-native:workspacesweb:getNetworkSettings", args ?? new GetNetworkSettingsArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::WorkSpacesWeb::NetworkSettings Resource Type
        /// </summary>
        public static Output<GetNetworkSettingsResult> Invoke(GetNetworkSettingsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkSettingsResult>("aws-native:workspacesweb:getNetworkSettings", args ?? new GetNetworkSettingsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkSettingsArgs : global::Pulumi.InvokeArgs
    {
        [Input("networkSettingsArn", required: true)]
        public string NetworkSettingsArn { get; set; } = null!;

        public GetNetworkSettingsArgs()
        {
        }
        public static new GetNetworkSettingsArgs Empty => new GetNetworkSettingsArgs();
    }

    public sealed class GetNetworkSettingsInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("networkSettingsArn", required: true)]
        public Input<string> NetworkSettingsArn { get; set; } = null!;

        public GetNetworkSettingsInvokeArgs()
        {
        }
        public static new GetNetworkSettingsInvokeArgs Empty => new GetNetworkSettingsInvokeArgs();
    }


    [OutputType]
    public sealed class GetNetworkSettingsResult
    {
        public readonly ImmutableArray<string> AssociatedPortalArns;
        public readonly string? NetworkSettingsArn;
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly ImmutableArray<string> SubnetIds;
        public readonly ImmutableArray<Outputs.NetworkSettingsTag> Tags;
        public readonly string? VpcId;

        [OutputConstructor]
        private GetNetworkSettingsResult(
            ImmutableArray<string> associatedPortalArns,

            string? networkSettingsArn,

            ImmutableArray<string> securityGroupIds,

            ImmutableArray<string> subnetIds,

            ImmutableArray<Outputs.NetworkSettingsTag> tags,

            string? vpcId)
        {
            AssociatedPortalArns = associatedPortalArns;
            NetworkSettingsArn = networkSettingsArn;
            SecurityGroupIds = securityGroupIds;
            SubnetIds = subnetIds;
            Tags = tags;
            VpcId = vpcId;
        }
    }
}
