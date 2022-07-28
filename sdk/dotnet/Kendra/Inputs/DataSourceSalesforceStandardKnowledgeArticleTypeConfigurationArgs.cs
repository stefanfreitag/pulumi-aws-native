// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceSalesforceStandardKnowledgeArticleTypeConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("documentDataFieldName", required: true)]
        public Input<string> DocumentDataFieldName { get; set; } = null!;

        [Input("documentTitleFieldName")]
        public Input<string>? DocumentTitleFieldName { get; set; }

        [Input("fieldMappings")]
        private InputList<Inputs.DataSourceToIndexFieldMappingArgs>? _fieldMappings;
        public InputList<Inputs.DataSourceToIndexFieldMappingArgs> FieldMappings
        {
            get => _fieldMappings ?? (_fieldMappings = new InputList<Inputs.DataSourceToIndexFieldMappingArgs>());
            set => _fieldMappings = value;
        }

        public DataSourceSalesforceStandardKnowledgeArticleTypeConfigurationArgs()
        {
        }
        public static new DataSourceSalesforceStandardKnowledgeArticleTypeConfigurationArgs Empty => new DataSourceSalesforceStandardKnowledgeArticleTypeConfigurationArgs();
    }
}
