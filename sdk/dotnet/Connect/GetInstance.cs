// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    public static class GetInstance
    {
        /// <summary>
        /// Resource Type definition for AWS::Connect::Instance
        /// </summary>
        public static Task<GetInstanceResult> InvokeAsync(GetInstanceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetInstanceResult>("aws-native:connect:getInstance", args ?? new GetInstanceArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Connect::Instance
        /// </summary>
        public static Output<GetInstanceResult> Invoke(GetInstanceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetInstanceResult>("aws-native:connect:getInstance", args ?? new GetInstanceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInstanceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// An instanceArn is automatically generated on creation based on instanceId.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetInstanceArgs()
        {
        }
        public static new GetInstanceArgs Empty => new GetInstanceArgs();
    }

    public sealed class GetInstanceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// An instanceArn is automatically generated on creation based on instanceId.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetInstanceInvokeArgs()
        {
        }
        public static new GetInstanceInvokeArgs Empty => new GetInstanceInvokeArgs();
    }


    [OutputType]
    public sealed class GetInstanceResult
    {
        /// <summary>
        /// An instanceArn is automatically generated on creation based on instanceId.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The attributes for the instance.
        /// </summary>
        public readonly Outputs.InstanceAttributes? Attributes;
        /// <summary>
        /// Timestamp of instance creation logged as part of instance creation.
        /// </summary>
        public readonly string? CreatedTime;
        /// <summary>
        /// An instanceId is automatically generated on creation and assigned as the unique identifier.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Specifies the creation status of new instance.
        /// </summary>
        public readonly Pulumi.AwsNative.Connect.InstanceStatus? InstanceStatus;
        /// <summary>
        /// Service linked role created as part of instance creation.
        /// </summary>
        public readonly string? ServiceRole;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetInstanceResult(
            string? arn,

            Outputs.InstanceAttributes? attributes,

            string? createdTime,

            string? id,

            Pulumi.AwsNative.Connect.InstanceStatus? instanceStatus,

            string? serviceRole,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Arn = arn;
            Attributes = attributes;
            CreatedTime = createdTime;
            Id = id;
            InstanceStatus = instanceStatus;
            ServiceRole = serviceRole;
            Tags = tags;
        }
    }
}
