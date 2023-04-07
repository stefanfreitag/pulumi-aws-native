// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EventSchemas
{
    public static class GetSchema
    {
        /// <summary>
        /// Resource Type definition for AWS::EventSchemas::Schema
        /// </summary>
        public static Task<GetSchemaResult> InvokeAsync(GetSchemaArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSchemaResult>("aws-native:eventschemas:getSchema", args ?? new GetSchemaArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EventSchemas::Schema
        /// </summary>
        public static Output<GetSchemaResult> Invoke(GetSchemaInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSchemaResult>("aws-native:eventschemas:getSchema", args ?? new GetSchemaInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSchemaArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetSchemaArgs()
        {
        }
        public static new GetSchemaArgs Empty => new GetSchemaArgs();
    }

    public sealed class GetSchemaInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetSchemaInvokeArgs()
        {
        }
        public static new GetSchemaInvokeArgs Empty => new GetSchemaInvokeArgs();
    }


    [OutputType]
    public sealed class GetSchemaResult
    {
        public readonly string? Content;
        public readonly string? Description;
        public readonly string? Id;
        public readonly string? SchemaArn;
        public readonly string? SchemaVersion;
        public readonly ImmutableArray<Outputs.SchemaTagsEntry> Tags;
        public readonly string? Type;

        [OutputConstructor]
        private GetSchemaResult(
            string? content,

            string? description,

            string? id,

            string? schemaArn,

            string? schemaVersion,

            ImmutableArray<Outputs.SchemaTagsEntry> tags,

            string? type)
        {
            Content = content;
            Description = description;
            Id = id;
            SchemaArn = schemaArn;
            SchemaVersion = schemaVersion;
            Tags = tags;
            Type = type;
        }
    }
}
