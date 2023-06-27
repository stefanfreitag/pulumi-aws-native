// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeBuild
{
    public static class GetSourceCredential
    {
        /// <summary>
        /// Resource Type definition for AWS::CodeBuild::SourceCredential
        /// </summary>
        public static Task<GetSourceCredentialResult> InvokeAsync(GetSourceCredentialArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSourceCredentialResult>("aws-native:codebuild:getSourceCredential", args ?? new GetSourceCredentialArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CodeBuild::SourceCredential
        /// </summary>
        public static Output<GetSourceCredentialResult> Invoke(GetSourceCredentialInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSourceCredentialResult>("aws-native:codebuild:getSourceCredential", args ?? new GetSourceCredentialInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSourceCredentialArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetSourceCredentialArgs()
        {
        }
        public static new GetSourceCredentialArgs Empty => new GetSourceCredentialArgs();
    }

    public sealed class GetSourceCredentialInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetSourceCredentialInvokeArgs()
        {
        }
        public static new GetSourceCredentialInvokeArgs Empty => new GetSourceCredentialInvokeArgs();
    }


    [OutputType]
    public sealed class GetSourceCredentialResult
    {
        public readonly string? AuthType;
        public readonly string? Id;
        public readonly string? Token;
        public readonly string? Username;

        [OutputConstructor]
        private GetSourceCredentialResult(
            string? authType,

            string? id,

            string? token,

            string? username)
        {
            AuthType = authType;
            Id = id;
            Token = token;
            Username = username;
        }
    }
}
