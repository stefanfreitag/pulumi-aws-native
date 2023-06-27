// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IAM
{
    public static class GetUserToGroupAddition
    {
        /// <summary>
        /// Resource Type definition for AWS::IAM::UserToGroupAddition
        /// </summary>
        public static Task<GetUserToGroupAdditionResult> InvokeAsync(GetUserToGroupAdditionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserToGroupAdditionResult>("aws-native:iam:getUserToGroupAddition", args ?? new GetUserToGroupAdditionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IAM::UserToGroupAddition
        /// </summary>
        public static Output<GetUserToGroupAdditionResult> Invoke(GetUserToGroupAdditionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserToGroupAdditionResult>("aws-native:iam:getUserToGroupAddition", args ?? new GetUserToGroupAdditionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserToGroupAdditionArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetUserToGroupAdditionArgs()
        {
        }
        public static new GetUserToGroupAdditionArgs Empty => new GetUserToGroupAdditionArgs();
    }

    public sealed class GetUserToGroupAdditionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetUserToGroupAdditionInvokeArgs()
        {
        }
        public static new GetUserToGroupAdditionInvokeArgs Empty => new GetUserToGroupAdditionInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserToGroupAdditionResult
    {
        public readonly string? GroupName;
        public readonly string? Id;
        public readonly ImmutableArray<string> Users;

        [OutputConstructor]
        private GetUserToGroupAdditionResult(
            string? groupName,

            string? id,

            ImmutableArray<string> users)
        {
            GroupName = groupName;
            Id = id;
            Users = users;
        }
    }
}
