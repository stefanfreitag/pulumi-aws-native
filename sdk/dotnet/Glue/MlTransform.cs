// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    /// <summary>
    /// Resource Type definition for AWS::Glue::MLTransform
    /// </summary>
    [Obsolete(@"MlTransform is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:glue:MlTransform")]
    public partial class MlTransform : global::Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("glueVersion")]
        public Output<string?> GlueVersion { get; private set; } = null!;

        [Output("inputRecordTables")]
        public Output<Outputs.MlTransformInputRecordTables> InputRecordTables { get; private set; } = null!;

        [Output("maxCapacity")]
        public Output<double?> MaxCapacity { get; private set; } = null!;

        [Output("maxRetries")]
        public Output<int?> MaxRetries { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("numberOfWorkers")]
        public Output<int?> NumberOfWorkers { get; private set; } = null!;

        [Output("role")]
        public Output<string> Role { get; private set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::MLTransform` for more information about the expected schema for this property.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        [Output("timeout")]
        public Output<int?> Timeout { get; private set; } = null!;

        [Output("transformEncryption")]
        public Output<Outputs.MlTransformTransformEncryption?> TransformEncryption { get; private set; } = null!;

        [Output("transformParameters")]
        public Output<Outputs.MlTransformTransformParameters> TransformParameters { get; private set; } = null!;

        [Output("workerType")]
        public Output<string?> WorkerType { get; private set; } = null!;


        /// <summary>
        /// Create a MlTransform resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MlTransform(string name, MlTransformArgs args, CustomResourceOptions? options = null)
            : base("aws-native:glue:MlTransform", name, args ?? new MlTransformArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MlTransform(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:glue:MlTransform", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "inputRecordTables",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing MlTransform resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MlTransform Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new MlTransform(name, id, options);
        }
    }

    public sealed class MlTransformArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("glueVersion")]
        public Input<string>? GlueVersion { get; set; }

        [Input("inputRecordTables", required: true)]
        public Input<Inputs.MlTransformInputRecordTablesArgs> InputRecordTables { get; set; } = null!;

        [Input("maxCapacity")]
        public Input<double>? MaxCapacity { get; set; }

        [Input("maxRetries")]
        public Input<int>? MaxRetries { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("numberOfWorkers")]
        public Input<int>? NumberOfWorkers { get; set; }

        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::MLTransform` for more information about the expected schema for this property.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        [Input("transformEncryption")]
        public Input<Inputs.MlTransformTransformEncryptionArgs>? TransformEncryption { get; set; }

        [Input("transformParameters", required: true)]
        public Input<Inputs.MlTransformTransformParametersArgs> TransformParameters { get; set; } = null!;

        [Input("workerType")]
        public Input<string>? WorkerType { get; set; }

        public MlTransformArgs()
        {
        }
        public static new MlTransformArgs Empty => new MlTransformArgs();
    }
}
