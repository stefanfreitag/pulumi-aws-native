// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetTrafficMirrorTarget
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::TrafficMirrorTarget
        /// </summary>
        public static Task<GetTrafficMirrorTargetResult> InvokeAsync(GetTrafficMirrorTargetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTrafficMirrorTargetResult>("aws-native:ec2:getTrafficMirrorTarget", args ?? new GetTrafficMirrorTargetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::TrafficMirrorTarget
        /// </summary>
        public static Output<GetTrafficMirrorTargetResult> Invoke(GetTrafficMirrorTargetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTrafficMirrorTargetResult>("aws-native:ec2:getTrafficMirrorTarget", args ?? new GetTrafficMirrorTargetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTrafficMirrorTargetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetTrafficMirrorTargetArgs()
        {
        }
        public static new GetTrafficMirrorTargetArgs Empty => new GetTrafficMirrorTargetArgs();
    }

    public sealed class GetTrafficMirrorTargetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetTrafficMirrorTargetInvokeArgs()
        {
        }
        public static new GetTrafficMirrorTargetInvokeArgs Empty => new GetTrafficMirrorTargetInvokeArgs();
    }


    [OutputType]
    public sealed class GetTrafficMirrorTargetResult
    {
        public readonly string? Id;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetTrafficMirrorTargetResult(
            string? id,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Id = id;
            Tags = tags;
        }
    }
}
