// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    public static class GetContactFlow
    {
        /// <summary>
        /// Resource Type definition for AWS::Connect::ContactFlow
        /// </summary>
        public static Task<GetContactFlowResult> InvokeAsync(GetContactFlowArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetContactFlowResult>("aws-native:connect:getContactFlow", args ?? new GetContactFlowArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Connect::ContactFlow
        /// </summary>
        public static Output<GetContactFlowResult> Invoke(GetContactFlowInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetContactFlowResult>("aws-native:connect:getContactFlow", args ?? new GetContactFlowInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetContactFlowArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The identifier of the contact flow (ARN).
        /// </summary>
        [Input("contactFlowArn", required: true)]
        public string ContactFlowArn { get; set; } = null!;

        public GetContactFlowArgs()
        {
        }
        public static new GetContactFlowArgs Empty => new GetContactFlowArgs();
    }

    public sealed class GetContactFlowInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The identifier of the contact flow (ARN).
        /// </summary>
        [Input("contactFlowArn", required: true)]
        public Input<string> ContactFlowArn { get; set; } = null!;

        public GetContactFlowInvokeArgs()
        {
        }
        public static new GetContactFlowInvokeArgs Empty => new GetContactFlowInvokeArgs();
    }


    [OutputType]
    public sealed class GetContactFlowResult
    {
        /// <summary>
        /// The identifier of the contact flow (ARN).
        /// </summary>
        public readonly string? ContactFlowArn;
        /// <summary>
        /// The content of the contact flow in JSON format.
        /// </summary>
        public readonly string? Content;
        /// <summary>
        /// The description of the contact flow.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The identifier of the Amazon Connect instance (ARN).
        /// </summary>
        public readonly string? InstanceArn;
        /// <summary>
        /// The name of the contact flow.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The state of the contact flow.
        /// </summary>
        public readonly Pulumi.AwsNative.Connect.ContactFlowState? State;
        /// <summary>
        /// One or more tags.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetContactFlowResult(
            string? contactFlowArn,

            string? content,

            string? description,

            string? instanceArn,

            string? name,

            Pulumi.AwsNative.Connect.ContactFlowState? state,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            ContactFlowArn = contactFlowArn;
            Content = content;
            Description = description;
            InstanceArn = instanceArn;
            Name = name;
            State = state;
            Tags = tags;
        }
    }
}
