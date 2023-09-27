// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Kendra DataSource
 */
export class DataSource extends pulumi.CustomResource {
    /**
     * Get an existing DataSource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataSource {
        return new DataSource(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:kendra:DataSource';

    /**
     * Returns true if the given object is an instance of DataSource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataSource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataSource.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly customDocumentEnrichmentConfiguration!: pulumi.Output<outputs.kendra.DataSourceCustomDocumentEnrichmentConfiguration | undefined>;
    public readonly dataSourceConfiguration!: pulumi.Output<outputs.kendra.DataSourceConfiguration | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly indexId!: pulumi.Output<string>;
    public readonly languageCode!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly roleArn!: pulumi.Output<string | undefined>;
    public readonly schedule!: pulumi.Output<string | undefined>;
    /**
     * Tags for labeling the data source
     */
    public readonly tags!: pulumi.Output<outputs.kendra.DataSourceTag[] | undefined>;
    public readonly type!: pulumi.Output<enums.kendra.DataSourceType>;

    /**
     * Create a DataSource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DataSourceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.indexId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'indexId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["customDocumentEnrichmentConfiguration"] = args ? args.customDocumentEnrichmentConfiguration : undefined;
            resourceInputs["dataSourceConfiguration"] = args ? args.dataSourceConfiguration : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["indexId"] = args ? args.indexId : undefined;
            resourceInputs["languageCode"] = args ? args.languageCode : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["schedule"] = args ? args.schedule : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["customDocumentEnrichmentConfiguration"] = undefined /*out*/;
            resourceInputs["dataSourceConfiguration"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["indexId"] = undefined /*out*/;
            resourceInputs["languageCode"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["schedule"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["type"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DataSource.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataSource resource.
 */
export interface DataSourceArgs {
    customDocumentEnrichmentConfiguration?: pulumi.Input<inputs.kendra.DataSourceCustomDocumentEnrichmentConfigurationArgs>;
    dataSourceConfiguration?: pulumi.Input<inputs.kendra.DataSourceConfigurationArgs>;
    description?: pulumi.Input<string>;
    indexId: pulumi.Input<string>;
    languageCode?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    roleArn?: pulumi.Input<string>;
    schedule?: pulumi.Input<string>;
    /**
     * Tags for labeling the data source
     */
    tags?: pulumi.Input<pulumi.Input<inputs.kendra.DataSourceTagArgs>[]>;
    type: pulumi.Input<enums.kendra.DataSourceType>;
}
