// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataBrew
{
    /// <summary>
    /// Resource schema for AWS::DataBrew::Job.
    /// </summary>
    [AwsNativeResourceType("aws-native:databrew:Job")]
    public partial class Job : global::Pulumi.CustomResource
    {
        [Output("dataCatalogOutputs")]
        public Output<ImmutableArray<Outputs.JobDataCatalogOutput>> DataCatalogOutputs { get; private set; } = null!;

        [Output("databaseOutputs")]
        public Output<ImmutableArray<Outputs.JobDatabaseOutput>> DatabaseOutputs { get; private set; } = null!;

        /// <summary>
        /// Dataset name
        /// </summary>
        [Output("datasetName")]
        public Output<string?> DatasetName { get; private set; } = null!;

        /// <summary>
        /// Encryption Key Arn
        /// </summary>
        [Output("encryptionKeyArn")]
        public Output<string?> EncryptionKeyArn { get; private set; } = null!;

        /// <summary>
        /// Encryption mode
        /// </summary>
        [Output("encryptionMode")]
        public Output<Pulumi.AwsNative.DataBrew.JobEncryptionMode?> EncryptionMode { get; private set; } = null!;

        /// <summary>
        /// Job Sample
        /// </summary>
        [Output("jobSample")]
        public Output<Outputs.JobSample?> JobSample { get; private set; } = null!;

        /// <summary>
        /// Log subscription
        /// </summary>
        [Output("logSubscription")]
        public Output<Pulumi.AwsNative.DataBrew.JobLogSubscription?> LogSubscription { get; private set; } = null!;

        /// <summary>
        /// Max capacity
        /// </summary>
        [Output("maxCapacity")]
        public Output<int?> MaxCapacity { get; private set; } = null!;

        /// <summary>
        /// Max retries
        /// </summary>
        [Output("maxRetries")]
        public Output<int?> MaxRetries { get; private set; } = null!;

        /// <summary>
        /// Job name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Output location
        /// </summary>
        [Output("outputLocation")]
        public Output<Outputs.JobOutputLocation?> OutputLocation { get; private set; } = null!;

        [Output("outputs")]
        public Output<ImmutableArray<Outputs.JobOutput>> Outputs { get; private set; } = null!;

        /// <summary>
        /// Profile Job configuration
        /// </summary>
        [Output("profileConfiguration")]
        public Output<Outputs.JobProfileConfiguration?> ProfileConfiguration { get; private set; } = null!;

        /// <summary>
        /// Project name
        /// </summary>
        [Output("projectName")]
        public Output<string?> ProjectName { get; private set; } = null!;

        [Output("recipe")]
        public Output<Outputs.JobRecipe?> Recipe { get; private set; } = null!;

        /// <summary>
        /// Role arn
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.CreateOnlyTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Timeout
        /// </summary>
        [Output("timeout")]
        public Output<int?> Timeout { get; private set; } = null!;

        /// <summary>
        /// Job type
        /// </summary>
        [Output("type")]
        public Output<Pulumi.AwsNative.DataBrew.JobType> Type { get; private set; } = null!;

        /// <summary>
        /// Data quality rules configuration
        /// </summary>
        [Output("validationConfigurations")]
        public Output<ImmutableArray<Outputs.JobValidationConfiguration>> ValidationConfigurations { get; private set; } = null!;


        /// <summary>
        /// Create a Job resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Job(string name, JobArgs args, CustomResourceOptions? options = null)
            : base("aws-native:databrew:Job", name, args ?? new JobArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Job(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:databrew:Job", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                    "tags[*]",
                    "type",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Job resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Job Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Job(name, id, options);
        }
    }

    public sealed class JobArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataCatalogOutputs")]
        private InputList<Inputs.JobDataCatalogOutputArgs>? _dataCatalogOutputs;
        public InputList<Inputs.JobDataCatalogOutputArgs> DataCatalogOutputs
        {
            get => _dataCatalogOutputs ?? (_dataCatalogOutputs = new InputList<Inputs.JobDataCatalogOutputArgs>());
            set => _dataCatalogOutputs = value;
        }

        [Input("databaseOutputs")]
        private InputList<Inputs.JobDatabaseOutputArgs>? _databaseOutputs;
        public InputList<Inputs.JobDatabaseOutputArgs> DatabaseOutputs
        {
            get => _databaseOutputs ?? (_databaseOutputs = new InputList<Inputs.JobDatabaseOutputArgs>());
            set => _databaseOutputs = value;
        }

        /// <summary>
        /// Dataset name
        /// </summary>
        [Input("datasetName")]
        public Input<string>? DatasetName { get; set; }

        /// <summary>
        /// Encryption Key Arn
        /// </summary>
        [Input("encryptionKeyArn")]
        public Input<string>? EncryptionKeyArn { get; set; }

        /// <summary>
        /// Encryption mode
        /// </summary>
        [Input("encryptionMode")]
        public Input<Pulumi.AwsNative.DataBrew.JobEncryptionMode>? EncryptionMode { get; set; }

        /// <summary>
        /// Job Sample
        /// </summary>
        [Input("jobSample")]
        public Input<Inputs.JobSampleArgs>? JobSample { get; set; }

        /// <summary>
        /// Log subscription
        /// </summary>
        [Input("logSubscription")]
        public Input<Pulumi.AwsNative.DataBrew.JobLogSubscription>? LogSubscription { get; set; }

        /// <summary>
        /// Max capacity
        /// </summary>
        [Input("maxCapacity")]
        public Input<int>? MaxCapacity { get; set; }

        /// <summary>
        /// Max retries
        /// </summary>
        [Input("maxRetries")]
        public Input<int>? MaxRetries { get; set; }

        /// <summary>
        /// Job name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Output location
        /// </summary>
        [Input("outputLocation")]
        public Input<Inputs.JobOutputLocationArgs>? OutputLocation { get; set; }

        [Input("outputs")]
        private InputList<Inputs.JobOutputArgs>? _outputs;
        public InputList<Inputs.JobOutputArgs> Outputs
        {
            get => _outputs ?? (_outputs = new InputList<Inputs.JobOutputArgs>());
            set => _outputs = value;
        }

        /// <summary>
        /// Profile Job configuration
        /// </summary>
        [Input("profileConfiguration")]
        public Input<Inputs.JobProfileConfigurationArgs>? ProfileConfiguration { get; set; }

        /// <summary>
        /// Project name
        /// </summary>
        [Input("projectName")]
        public Input<string>? ProjectName { get; set; }

        [Input("recipe")]
        public Input<Inputs.JobRecipeArgs>? Recipe { get; set; }

        /// <summary>
        /// Role arn
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.CreateOnlyTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// Timeout
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        /// <summary>
        /// Job type
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.DataBrew.JobType> Type { get; set; } = null!;

        [Input("validationConfigurations")]
        private InputList<Inputs.JobValidationConfigurationArgs>? _validationConfigurations;

        /// <summary>
        /// Data quality rules configuration
        /// </summary>
        public InputList<Inputs.JobValidationConfigurationArgs> ValidationConfigurations
        {
            get => _validationConfigurations ?? (_validationConfigurations = new InputList<Inputs.JobValidationConfigurationArgs>());
            set => _validationConfigurations = value;
        }

        public JobArgs()
        {
        }
        public static new JobArgs Empty => new JobArgs();
    }
}
