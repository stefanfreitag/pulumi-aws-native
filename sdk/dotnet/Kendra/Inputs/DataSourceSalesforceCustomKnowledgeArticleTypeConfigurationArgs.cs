// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceSalesforceCustomKnowledgeArticleTypeConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("documentDataFieldName", required: true)]
        public Input<string> DocumentDataFieldName { get; set; } = null!;

        [Input("documentTitleFieldName")]
        public Input<string>? DocumentTitleFieldName { get; set; }

        [Input("fieldMappings")]
        private InputList<Inputs.DataSourceDataSourceToIndexFieldMappingArgs>? _fieldMappings;
        public InputList<Inputs.DataSourceDataSourceToIndexFieldMappingArgs> FieldMappings
        {
            get => _fieldMappings ?? (_fieldMappings = new InputList<Inputs.DataSourceDataSourceToIndexFieldMappingArgs>());
            set => _fieldMappings = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public DataSourceSalesforceCustomKnowledgeArticleTypeConfigurationArgs()
        {
        }
    }
}
