// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeStar
{
    public static class GetGitHubRepository
    {
        /// <summary>
        /// Resource Type definition for AWS::CodeStar::GitHubRepository
        /// </summary>
        public static Task<GetGitHubRepositoryResult> InvokeAsync(GetGitHubRepositoryArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetGitHubRepositoryResult>("aws-native:codestar:getGitHubRepository", args ?? new GetGitHubRepositoryArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CodeStar::GitHubRepository
        /// </summary>
        public static Output<GetGitHubRepositoryResult> Invoke(GetGitHubRepositoryInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetGitHubRepositoryResult>("aws-native:codestar:getGitHubRepository", args ?? new GetGitHubRepositoryInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGitHubRepositoryArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetGitHubRepositoryArgs()
        {
        }
        public static new GetGitHubRepositoryArgs Empty => new GetGitHubRepositoryArgs();
    }

    public sealed class GetGitHubRepositoryInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetGitHubRepositoryInvokeArgs()
        {
        }
        public static new GetGitHubRepositoryInvokeArgs Empty => new GetGitHubRepositoryInvokeArgs();
    }


    [OutputType]
    public sealed class GetGitHubRepositoryResult
    {
        public readonly Outputs.GitHubRepositoryCode? Code;
        public readonly string? ConnectionArn;
        public readonly bool? EnableIssues;
        public readonly string? Id;
        public readonly bool? IsPrivate;
        public readonly string? RepositoryAccessToken;
        public readonly string? RepositoryDescription;
        public readonly string? RepositoryName;
        public readonly string? RepositoryOwner;

        [OutputConstructor]
        private GetGitHubRepositoryResult(
            Outputs.GitHubRepositoryCode? code,

            string? connectionArn,

            bool? enableIssues,

            string? id,

            bool? isPrivate,

            string? repositoryAccessToken,

            string? repositoryDescription,

            string? repositoryName,

            string? repositoryOwner)
        {
            Code = code;
            ConnectionArn = connectionArn;
            EnableIssues = enableIssues;
            Id = id;
            IsPrivate = isPrivate;
            RepositoryAccessToken = repositoryAccessToken;
            RepositoryDescription = repositoryDescription;
            RepositoryName = repositoryName;
            RepositoryOwner = repositoryOwner;
        }
    }
}
