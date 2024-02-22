// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Transfer
{
    public static class GetUser
    {
        /// <summary>
        /// Resource Type definition for AWS::Transfer::User
        /// </summary>
        public static Task<GetUserResult> InvokeAsync(GetUserArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserResult>("aws-native:transfer:getUser", args ?? new GetUserArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Transfer::User
        /// </summary>
        public static Output<GetUserResult> Invoke(GetUserInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserResult>("aws-native:transfer:getUser", args ?? new GetUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetUserArgs()
        {
        }
        public static new GetUserArgs Empty => new GetUserArgs();
    }

    public sealed class GetUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetUserInvokeArgs()
        {
        }
        public static new GetUserInvokeArgs Empty => new GetUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserResult
    {
        public readonly string? Arn;
        public readonly string? HomeDirectory;
        public readonly ImmutableArray<Outputs.UserHomeDirectoryMapEntry> HomeDirectoryMappings;
        public readonly string? HomeDirectoryType;
        public readonly string? Id;
        public readonly string? Policy;
        public readonly Outputs.UserPosixProfile? PosixProfile;
        public readonly string? Role;
        public readonly ImmutableArray<Outputs.UserSshPublicKey> SshPublicKeys;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetUserResult(
            string? arn,

            string? homeDirectory,

            ImmutableArray<Outputs.UserHomeDirectoryMapEntry> homeDirectoryMappings,

            string? homeDirectoryType,

            string? id,

            string? policy,

            Outputs.UserPosixProfile? posixProfile,

            string? role,

            ImmutableArray<Outputs.UserSshPublicKey> sshPublicKeys,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Arn = arn;
            HomeDirectory = homeDirectory;
            HomeDirectoryMappings = homeDirectoryMappings;
            HomeDirectoryType = homeDirectoryType;
            Id = id;
            Policy = policy;
            PosixProfile = posixProfile;
            Role = role;
            SshPublicKeys = sshPublicKeys;
            Tags = tags;
        }
    }
}
