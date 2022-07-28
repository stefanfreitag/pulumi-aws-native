// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache
{
    public static class GetUserGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::ElastiCache::UserGroup
        /// </summary>
        public static Task<GetUserGroupResult> InvokeAsync(GetUserGroupArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUserGroupResult>("aws-native:elasticache:getUserGroup", args ?? new GetUserGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ElastiCache::UserGroup
        /// </summary>
        public static Output<GetUserGroupResult> Invoke(GetUserGroupInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetUserGroupResult>("aws-native:elasticache:getUserGroup", args ?? new GetUserGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the user group.
        /// </summary>
        [Input("userGroupId", required: true)]
        public string UserGroupId { get; set; } = null!;

        public GetUserGroupArgs()
        {
        }
        public static new GetUserGroupArgs Empty => new GetUserGroupArgs();
    }

    public sealed class GetUserGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the user group.
        /// </summary>
        [Input("userGroupId", required: true)]
        public Input<string> UserGroupId { get; set; } = null!;

        public GetUserGroupInvokeArgs()
        {
        }
        public static new GetUserGroupInvokeArgs Empty => new GetUserGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserGroupResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the user account.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Indicates user group status. Can be "creating", "active", "modifying", "deleting".
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// List of users associated to this user group.
        /// </summary>
        public readonly ImmutableArray<string> UserIds;

        [OutputConstructor]
        private GetUserGroupResult(
            string? arn,

            string? status,

            ImmutableArray<string> userIds)
        {
            Arn = arn;
            Status = status;
            UserIds = userIds;
        }
    }
}
