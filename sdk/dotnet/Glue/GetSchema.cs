// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    public static class GetSchema
    {
        /// <summary>
        /// This resource represents a schema of Glue Schema Registry.
        /// </summary>
        public static Task<GetSchemaResult> InvokeAsync(GetSchemaArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSchemaResult>("aws-native:glue:getSchema", args ?? new GetSchemaArgs(), options.WithDefaults());

        /// <summary>
        /// This resource represents a schema of Glue Schema Registry.
        /// </summary>
        public static Output<GetSchemaResult> Invoke(GetSchemaInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSchemaResult>("aws-native:glue:getSchema", args ?? new GetSchemaInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSchemaArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Amazon Resource Name for the Schema.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetSchemaArgs()
        {
        }
        public static new GetSchemaArgs Empty => new GetSchemaArgs();
    }

    public sealed class GetSchemaInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Amazon Resource Name for the Schema.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetSchemaInvokeArgs()
        {
        }
        public static new GetSchemaInvokeArgs Empty => new GetSchemaInvokeArgs();
    }


    [OutputType]
    public sealed class GetSchemaResult
    {
        /// <summary>
        /// Amazon Resource Name for the Schema.
        /// </summary>
        public readonly string? Arn;
        public readonly Outputs.SchemaVersion? CheckpointVersion;
        /// <summary>
        /// Compatibility setting for the schema.
        /// </summary>
        public readonly Pulumi.AwsNative.Glue.SchemaCompatibility? Compatibility;
        /// <summary>
        /// A description of the schema. If description is not provided, there will not be any default value for this.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Represents the version ID associated with the initial schema version.
        /// </summary>
        public readonly string? InitialSchemaVersionId;
        /// <summary>
        /// List of tags to tag the schema
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetSchemaResult(
            string? arn,

            Outputs.SchemaVersion? checkpointVersion,

            Pulumi.AwsNative.Glue.SchemaCompatibility? compatibility,

            string? description,

            string? initialSchemaVersionId,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Arn = arn;
            CheckpointVersion = checkpointVersion;
            Compatibility = compatibility;
            Description = description;
            InitialSchemaVersionId = initialSchemaVersionId;
            Tags = tags;
        }
    }
}
