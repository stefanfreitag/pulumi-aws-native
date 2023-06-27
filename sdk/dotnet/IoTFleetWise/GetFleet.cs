// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise
{
    public static class GetFleet
    {
        /// <summary>
        /// Definition of AWS::IoTFleetWise::Fleet Resource Type
        /// </summary>
        public static Task<GetFleetResult> InvokeAsync(GetFleetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFleetResult>("aws-native:iotfleetwise:getFleet", args ?? new GetFleetArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::IoTFleetWise::Fleet Resource Type
        /// </summary>
        public static Output<GetFleetResult> Invoke(GetFleetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFleetResult>("aws-native:iotfleetwise:getFleet", args ?? new GetFleetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFleetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetFleetArgs()
        {
        }
        public static new GetFleetArgs Empty => new GetFleetArgs();
    }

    public sealed class GetFleetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetFleetInvokeArgs()
        {
        }
        public static new GetFleetInvokeArgs Empty => new GetFleetInvokeArgs();
    }


    [OutputType]
    public sealed class GetFleetResult
    {
        public readonly string? Arn;
        public readonly string? CreationTime;
        public readonly string? Description;
        public readonly string? LastModificationTime;
        public readonly ImmutableArray<Outputs.FleetTag> Tags;

        [OutputConstructor]
        private GetFleetResult(
            string? arn,

            string? creationTime,

            string? description,

            string? lastModificationTime,

            ImmutableArray<Outputs.FleetTag> tags)
        {
            Arn = arn;
            CreationTime = creationTime;
            Description = description;
            LastModificationTime = lastModificationTime;
            Tags = tags;
        }
    }
}
