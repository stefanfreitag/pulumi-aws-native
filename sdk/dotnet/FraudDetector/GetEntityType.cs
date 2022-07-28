// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FraudDetector
{
    public static class GetEntityType
    {
        /// <summary>
        /// An entity type for fraud detector.
        /// </summary>
        public static Task<GetEntityTypeResult> InvokeAsync(GetEntityTypeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEntityTypeResult>("aws-native:frauddetector:getEntityType", args ?? new GetEntityTypeArgs(), options.WithDefaults());

        /// <summary>
        /// An entity type for fraud detector.
        /// </summary>
        public static Output<GetEntityTypeResult> Invoke(GetEntityTypeInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetEntityTypeResult>("aws-native:frauddetector:getEntityType", args ?? new GetEntityTypeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEntityTypeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The entity type ARN.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetEntityTypeArgs()
        {
        }
        public static new GetEntityTypeArgs Empty => new GetEntityTypeArgs();
    }

    public sealed class GetEntityTypeInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The entity type ARN.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetEntityTypeInvokeArgs()
        {
        }
        public static new GetEntityTypeInvokeArgs Empty => new GetEntityTypeInvokeArgs();
    }


    [OutputType]
    public sealed class GetEntityTypeResult
    {
        /// <summary>
        /// The entity type ARN.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The timestamp when the entity type was created.
        /// </summary>
        public readonly string? CreatedTime;
        /// <summary>
        /// The entity type description.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The timestamp when the entity type was last updated.
        /// </summary>
        public readonly string? LastUpdatedTime;
        /// <summary>
        /// Tags associated with this entity type.
        /// </summary>
        public readonly ImmutableArray<Outputs.EntityTypeTag> Tags;

        [OutputConstructor]
        private GetEntityTypeResult(
            string? arn,

            string? createdTime,

            string? description,

            string? lastUpdatedTime,

            ImmutableArray<Outputs.EntityTypeTag> tags)
        {
            Arn = arn;
            CreatedTime = createdTime;
            Description = description;
            LastUpdatedTime = lastUpdatedTime;
            Tags = tags;
        }
    }
}
