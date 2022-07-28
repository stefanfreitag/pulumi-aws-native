// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Macie
{
    public static class GetCustomDataIdentifier
    {
        /// <summary>
        /// Macie CustomDataIdentifier resource schema
        /// </summary>
        public static Task<GetCustomDataIdentifierResult> InvokeAsync(GetCustomDataIdentifierArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCustomDataIdentifierResult>("aws-native:macie:getCustomDataIdentifier", args ?? new GetCustomDataIdentifierArgs(), options.WithDefaults());

        /// <summary>
        /// Macie CustomDataIdentifier resource schema
        /// </summary>
        public static Output<GetCustomDataIdentifierResult> Invoke(GetCustomDataIdentifierInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetCustomDataIdentifierResult>("aws-native:macie:getCustomDataIdentifier", args ?? new GetCustomDataIdentifierInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCustomDataIdentifierArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Custom data identifier ID.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetCustomDataIdentifierArgs()
        {
        }
        public static new GetCustomDataIdentifierArgs Empty => new GetCustomDataIdentifierArgs();
    }

    public sealed class GetCustomDataIdentifierInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Custom data identifier ID.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetCustomDataIdentifierInvokeArgs()
        {
        }
        public static new GetCustomDataIdentifierInvokeArgs Empty => new GetCustomDataIdentifierInvokeArgs();
    }


    [OutputType]
    public sealed class GetCustomDataIdentifierResult
    {
        /// <summary>
        /// Custom data identifier ARN.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Custom data identifier ID.
        /// </summary>
        public readonly string? Id;

        [OutputConstructor]
        private GetCustomDataIdentifierResult(
            string? arn,

            string? id)
        {
            Arn = arn;
            Id = id;
        }
    }
}
